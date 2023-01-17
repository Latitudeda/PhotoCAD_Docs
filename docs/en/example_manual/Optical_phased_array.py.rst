Example: Optical Phased Array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The integrated optical phased array (OPA) enables low-loss beam steering compared to the Bulk optics system and has applications in the following areas:

* Sensing
* Imaging
* Light Detection and Ranging (LiDAR)
* Displays
* Telecommunications

**PhotoCAD** design automation platform is well suited for OPA design because it is developed and used in Python 3.X with a powerful ecosystem and third-party toolkit support, and can call on a variety of simulation software under Python 3.X to **update structural parameters and simulate in real time**. By learning how to create OPAs in code below, designers can extend simple design concepts to large designs that are easy to simulate.


Introduction
------------------------------------------
The optical phased array (OPA) consists of a split tree with each output connected to a ``tin_heater``, another port of the ``tin_heater`` will be connected to a ``GratingCoupler``, two ``electrical ports`` exist on each ``tin_heater``, and the ``electrical port`` is connected to the ``BondPad`` by the ``LinkBetween`` function.

Full script
-----------------------------------------
::

    from dataclasses import dataclass
    from typing import Mapping, cast

    import numpy
    import numpy as np
    from fnpcell import all as fp
    from gpdk import all as pdk
    from gpdk.technology import get_technology
    from gpdk.components.step.step2.mmi1x2 import MMI1x2


    @dataclass(eq=False)
    class MMITree(fp.PCell):
        x_spacing: float = fp.PositiveFloatParam(default=50)
        end_y_spacing: float = fp.PositiveFloatParam(default=100)
        order: float = fp.PositiveFloatParam(default=3)
        def build(self):
            insts, elems, ports = super().build()
            TECH = get_technology()

            x_spacing = self.x_spacing
            end_y_spacing = self.end_y_spacing
            order = self.order
            mmi = MMI1x2()
            num_per_col = []
            v_spacing = []

            for i in range(order):
                num_per_col.append(2**i)
                v_spacing.append(end_y_spacing*(2**(order - i - 1)))

            for i in range(order):
                for j in range(num_per_col[i]):
                    x = i * x_spacing
                    y = (-(num_per_col[i] - 1) * v_spacing[i]/2) + j * v_spacing[i] # bottom mmi y = 0
                    mmi = mmi["op_0"].repositioned(at=(x,y)).owner
                    insts += mmi, f"{i},{j}"



            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)

            # link every mmi together to become MMI tree
            for i in range(order):
                for j in range(num_per_col[i]):
                    if i < order-1:
                        link1 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_1"],
                                               end=mmi_tree[f"{i+1},{2*j}"]["op_0"],
                                               bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                        insts += link1
                        link2 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_2"],
                                               end=mmi_tree[f"{i+1},{2*j+1}"]["op_0"],
                                               bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                        insts += link2

            ports += mmi_tree["0,0"]["op_0"].with_name("op_0")
            # put ports on the last column of the tree
            for i in range(num_per_col[-1]):
                ports += mmi_tree[f"{order - 1},{i}"]["op_1"].with_name(f"op_{2*i+1}")
                ports += mmi_tree[f"{order - 1},{i}"]["op_2"].with_name(f"op_{2*i+2}")

            heater_wl = 1000
            heater_tl = 400
            heater = pdk.TiNHeaterwithep(waveguide_length=heater_wl, tin_length=heater_tl, tin_box_size=20, contact_box_size=20)

            # define heater positions
            for i in range (num_per_col[-1]):
                for j in range(2):
                    ht_x = mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"].position[0]
                    ht_y = mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"].position[1]
                    if j == 0:
                        heater = heater["op_0"].repositioned(at=(ht_x + 15*(2**order), ht_y - end_y_spacing / 4)).owner
                    else:
                        heater = heater["op_0"].repositioned(at=(ht_x + 15*(2**order), ht_y + end_y_spacing / 4)).owner
                    insts += heater, f"ht_{2*i+j},{0}"
            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)


            # link heater left port and mmi right ports
            for i in range(num_per_col[-1]):
                for j in range(2):
                    link3 = fp.LinkBetween(
                        start=mmi_tree[f"ht_{2*i+j},0"]["op_0"],
                        end=mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"],
                        bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR
                    )
                    insts += link3




            GC = pdk.GratingCoupler()
            GC_0 = GC.translated(150, 0).h_mirrored()
            insts += GC_0
            # link the left GC with the first MMI
            link4 = fp.LinkBetween(start=GC_0["op_0"], end=mmi_tree["0,0"]["op_0"], bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
            insts += link4

            # positioning every GC on the right of the circuit
            for i in range (num_per_col[-1]):
                for j in range(2):
                    gc_x = mmi_tree[f"ht_{2*i+j},0"]["op_1"].position[0]
                    gc_y = mmi_tree[f"ht_{2*i+j},0"]["op_1"].position[1]
                    GC = GC["op_0"].repositioned(at=(gc_x+15*(2**order), gc_y)).owner
                    insts += GC, f"gc_{i},{j+1}"
            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)
            # link heaters and gcs together
            for i in range(num_per_col[-1]):
                for j in range(2):
                    link5 = fp.LinkBetween(
                        start=mmi_tree[f"ht_{2*i+j},0"]["op_1"],
                        end=mmi_tree[f"gc_{i},{j+1}"]["op_0"],
                        bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR
                    )
                    insts += link5
            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)

            BP = pdk.BondPad(pad_width=75, pad_height=75)
            pads_x = numpy.linspace(100*(2 **(order)), 50, 2 **(order))
            pads_left_x = numpy.linspace(90*(2 **(order)), 50,  2 **(order))
            pads_right_x = numpy.linspace(50, 90*(2 **(order)), 2 **(order))
            # define all pads position (seperate left pad and right pads
            for i in range (2**(order)):
                bp_x = pads_left_x[i]
                bp_y = end_y_spacing * (2** (order-1)) / 2
                ht_left_x = mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_0"].position[0]
                BP_left = BP["ep_0"].repositioned(at=(ht_left_x-bp_x, bp_y+15*(2**order+1)+100)).owner
                insts += BP_left, f"BP_{i},0"
            for i in range (2**(order)):
                bp_x = pads_right_x[i]
                bp_y = end_y_spacing * (2 ** (order - 1)) / 2
                ht_right_x = mmi_tree[f"ht_{2**(order)-1},0"]["ep_1"].position[0]
                BP_right = BP["ep_0"].repositioned(at=(bp_x+ht_right_x, bp_y + 15*(2**order+1)+100)).owner
                insts += BP_right, f"BP_{i},1"
            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)

            # link left pads with heater left port
            for i in range(2**(order)):
                    link6 = fp.LinkBetween(
                            start=mmi_tree[f"BP_{i},0"]["ep_0"].with_orientation(degrees=-90),
                            end=mmi_tree[f"ht_{i},0"]["ep_0"].with_orientation(degrees=180),
                            metal_line_type=TECH.METAL.M2.W10,
                            min_distance=50,
                            waypoints=[
                                fp.Waypoint(mmi_tree[f"BP_{i},0"]["ep_0"].position[0],mmi_tree[f"BP_{i},0"]["ep_0"].position[1]-37.5-15*(2**(order)-i), -90),

                                fp.Waypoint(mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_0"].position[0]-15*(2**(order)-i),end_y_spacing * (2** (order-1)) / 2, -90)
                            ]

                        )
                    insts += link6
            # link right pads with heater right port
            for i in range(2**(order)):
                     link7 = fp.LinkBetween(
                         start=mmi_tree[f"BP_{i},1"]["ep_0"].with_orientation(degrees=-90),
                         end=mmi_tree[f"ht_{2**(order)-1-i},0"]["ep_1"].with_orientation(
                             degrees=0),
                         metal_line_type=TECH.METAL.M2.W10,
                         min_distance=50,
                         waypoints=[
                             fp.Waypoint(mmi_tree[f"BP_{i},1"]["ep_0"].position[0],
                                         mmi_tree[f"BP_{i},1"]["ep_0"].position[1] - 37.5 - 15 * (i+1),
                                         -90),

                             fp.Waypoint(
                                 mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_1"].position[0] + 15 * (i+1),
                                 end_y_spacing * (2 ** (order - 1)) / 2, -90)
                         ]

                     )
                     insts += link7
            fmt: on
            return insts, elems, ports
    #

    if __name__ == "__main__":
        from pathlib import Path

        gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
        library = fp.Library()

        TECH = get_technology()
        # =============================================================
        # fmt: off

        library += MMITree()

        # fmt: on
        # =============================================================
        fp.export_gds(library, file=gds_file)
        # fp.plot(library)
        # print(MMITree())

Run the complete script once, generating the following GDS layout.    

.. image:: ../example_image/opa1.png

Generation and arrangement of MMI tree
--------------------------------------------------
First of all, we need to create the MMI tree, and generate the devices by calling ``MMI1x2()`` through ``pdk``, we use ``order`` as the MMI level, ``end_y_spacing`` represents the spacing between the devices at the last level of the MMI tree, they are all equally spaced, and ``x_spacing`` represents the horizontal spaces between each ``MMI1x2`` device.
The value of ``order`` is 3, which means that the whole MMI tree is split twice from 1 device, in other words, three columns of MMI devices will be generated, as shown in the following figure.

::

    mmi = MMI1x2()
    x_spacing: float = fp.PositiveFloatParam(default=50)
    end_y_spacing: float = fp.PositiveFloatParam(default=100)
    order: float = fp.PositiveFloatParam(default=3)
    
    
.. image:: ../example_image/opa2.png    
    
Users can adjust the ``order`` according to their needs. We run the program after adjusting ``order`` to 4 and get the following figure.

.. image:: ../example_image/opa3.png

Next, the script that generates the MMI tree is analyzed. The first for loop is used to generate x/y corordinates for MMI to be positioned. ``num_per_col`` represents the amount of MMI in the order, and ``v_spacing`` represents the vertical distance between the Nth MMI and the bottom MMI.

::

        num_per_col = []
        v_spacing = []

        for i in range(order):
            num_per_col.append(2**i)
            v_spacing.append(end_y_spacing*(2**(order - i - 1)))
            
            

The second for loop is used to position every MMI based on the above scripts. Note that the lowest MMI is where y=0 is located. Here we name the MMIs ``[i,j]``, which means that the MMI is in the ``i`` row and located at the ``j``th counted from bottom to top.

::

        for i in range(order):
            for j in range(num_per_col[i]):
                x = i * x_spacing
                y = (-(num_per_col[i] - 1) * v_spacing[i]/2) + j * v_spacing[i] # bottom mmi y = 0
                mmi = mmi["op_0"].repositioned(at=(x,y)).owner
                insts += mmi, f"{i},{j}"
        mmi_tree = cast(Mapping[str, fp.ICellRef], insts)
        
        

After the placement of every MMIs, we connect the ports using the ``LinkBetween`` function. Two different links represents that the output of one MMI will be seperated into two connections, one to the upwards MMI and another to the downwards of the MMI located at the next row. 

::

         for i in range(order):
                    for j in range(num_per_col[i]):
                        if i < order-1:
                            link1 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_1"],
                                                   end=mmi_tree[f"{i+1},{2*j}"]["op_0"],
                                                   bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                            insts += link1
                            link2 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_2"],
                                                   end=mmi_tree[f"{i+1},{2*j+1}"]["op_0"],
                                                   bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                            insts += link2
                            
                            
                            
Generation and arrangement of Heaters and GratingCouplers
----------------------------------------------------------------------------------
Define the dimensions of ``heater`` by ``heater_wl`` and ``heater_tl``, and then generate the corresponding ``GratingCoupler`` at the back of each MMI
by for loop. The x and y coordinates of the placement of the ``GC`` and ``heater`` are partly provided by the port of each MMI by the ``.position`` method, which obtains the MMI port center position ( ``ht_x``, ``ht_y``). Both ``heater`` and ``GC`` positions are extended to a certain distance due to the routing of the metal wire.   

::

        heater_wl = 1000
        heater_tl = 400
        heater = pdk.TiNHeaterwithep(waveguide_length=heater_wl, tin_length=heater_tl, tin_box_size=20, contact_box_size=20)

        # define heater positions
        for i in range (num_per_col[-1]):
            for j in range(2):
                ht_x = mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"].position[0]
                ht_y = mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"].position[1]
                if j == 0:
                    heater = heater["op_0"].repositioned(at=(ht_x + 15*(2**order), ht_y - end_y_spacing / 4)).owner
                else:
                    heater = heater["op_0"].repositioned(at=(ht_x + 15*(2**order), ht_y + end_y_spacing / 4)).owner
                insts += heater, f"ht_{2*i+j},{0}"
        mmi_tree = cast(Mapping[str, fp.ICellRef], insts)


        # link heater left port and mmi right ports
        for i in range(num_per_col[-1]):
            for j in range(2):
                link3 = fp.LinkBetween(
                    start=mmi_tree[f"ht_{2*i+j},0"]["op_0"],
                    end=mmi_tree[f"{order - 1},{i}"][f"op_{j+1}"],
                    bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR
                )
                insts += link3




        GC = pdk.GratingCoupler()
        GC_0 = GC.translated(150, 0).h_mirrored()
        insts += GC_0
        # link the left GC with the first MMI
        link4 = fp.LinkBetween(start=GC_0["op_0"], end=mmi_tree["0,0"]["op_0"], bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
        insts += link4

        # positioning every GC on the right of the circuit
        for i in range (num_per_col[-1]):
            for j in range(2):
                gc_x = mmi_tree[f"ht_{2*i+j},0"]["op_1"].position[0]
                gc_y = mmi_tree[f"ht_{2*i+j},0"]["op_1"].position[1]
                GC = GC["op_0"].repositioned(at=(gc_x+15*(2**order), gc_y)).owner
                insts += GC, f"gc_{i},{j+1}"
        mmi_tree = cast(Mapping[str, fp.ICellRef], insts)
        # link heaters and gcs together
        for i in range(num_per_col[-1]):
            for j in range(2):
                link5 = fp.LinkBetween(
                    start=mmi_tree[f"ht_{2*i+j},0"]["op_1"],
                    end=mmi_tree[f"gc_{i},{j+1}"]["op_0"],
                    bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR
                )
                insts += link5
        mmi_tree = cast(Mapping[str, fp.ICellRef], insts)
        
        
BondPad arrangement and metal wire routing
----------------------------------------------------------
Until now, we have finished the optical waveguide routing of the OPA. Next we have to generate the ``BondPad`` on top of the layout to connect the heater pins with the outside world. The horizontal coordinates of the ``BondPad`` are generated by linspace to get equally spaced horizontal coordinates. The left part and the right part of the pads will be discussed seperately.  Then use the for loop to generate the number of BondPads related to the level of the MMI tree.



::

        BP = pdk.BondPad(pad_width=75, pad_height=75)
        pads_left_x = numpy.linspace(90*(2 **(order)), 50,  2 **(order))
        pads_right_x = numpy.linspace(50, 90*(2 **(order)), 2 **(order))
        # define all pads position (seperate left pad and right pads
        for i in range (2**(order)):
            bp_x = pads_left_x[i]
            bp_y = end_y_spacing * (2** (order-1)) / 2
            ht_left_x = mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_0"].position[0]
            BP_left = BP["ep_0"].repositioned(at=(ht_left_x-bp_x, bp_y+15*(2**order+1)+100)).owner
            insts += BP_left, f"BP_{i},0"
        for i in range (2**(order)):
            bp_x = pads_right_x[i]
            bp_y = end_y_spacing * (2 ** (order - 1)) / 2
            ht_right_x = mmi_tree[f"ht_{2**(order)-1},0"]["ep_1"].position[0]
            BP_right = BP["ep_0"].repositioned(at=(bp_x+ht_right_x, bp_y + 15*(2**order+1)+100)).owner
            insts += BP_right, f"BP_{i},1"
        mmi_tree = cast(Mapping[str, fp.ICellRef], insts)



Then the ``BondPad`` are be conected to the pins on the ``heater`` using ``LinkBetween`` function. To avoid short when the crossing of the metal wire appears, ``waypoints`` are being set and depends on the distance between the pins and the ``BondPads``. When those are close to each other, the x-coordinate of the ``waypoint`` will be also close to the pins, meaning that a quick turn will be generate through the connection. The ``waypoints`` are also set to minimize the overlapping between the metal wires and the optical waveguides to avoid heat effect to the material property of the optical wg.



::

        # link left pads with heater left port
        for i in range(2**(order)):
                link6 = fp.LinkBetween(
                        start=mmi_tree[f"BP_{i},0"]["ep_0"].with_orientation(degrees=-90),
                        end=mmi_tree[f"ht_{i},0"]["ep_0"].with_orientation(degrees=180),
                        metal_line_type=TECH.METAL.M2.W10,
                        min_distance=50,
                        waypoints=[
                            fp.Waypoint(mmi_tree[f"BP_{i},0"]["ep_0"].position[0],mmi_tree[f"BP_{i},0"]["ep_0"].position[1]-37.5-15*(2**(order)-i), -90),

                            fp.Waypoint(mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_0"].position[0]-15*(2**(order)-i),end_y_spacing * (2** (order-1)) / 2, -90)
                        ]

                    )
                insts += link6
        # link right pads with heater right port
        for i in range(2**(order)):
                 link7 = fp.LinkBetween(
                     start=mmi_tree[f"BP_{i},1"]["ep_0"].with_orientation(degrees=-90),
                     end=mmi_tree[f"ht_{2**(order)-1-i},0"]["ep_1"].with_orientation(
                         degrees=0),
                     metal_line_type=TECH.METAL.M2.W10,
                     min_distance=50,
                     waypoints=[
                         fp.Waypoint(mmi_tree[f"BP_{i},1"]["ep_0"].position[0],
                                     mmi_tree[f"BP_{i},1"]["ep_0"].position[1] - 37.5 - 15 * (i+1),
                                     -90),

                         fp.Waypoint(
                             mmi_tree[f"ht_{2 ** (order) - 1},0"]["ep_1"].position[0] + 15 * (i+1),
                             end_y_spacing * (2 ** (order - 1)) / 2, -90)
                     ]

                 )
                 insts += link7
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
