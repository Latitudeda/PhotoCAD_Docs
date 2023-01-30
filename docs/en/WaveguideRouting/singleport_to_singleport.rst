Single-port to Single-port
====================


There are a total of three types of connections from single port to single port:

1. ``fp.LinkBetween``
2. ``TECH.LINKER``
3. ``>>``

Here's a comparison of the three options

.. image:: ../images/one_port_to_one_port_en.png

Among them, ``LinkBetween`` is relatively flexible and ``LINKER`` is relatively short and neat.

Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    # Interconnecting device ports by calling fp.create_links 
    device = fp.create_links(
        link_type=TECH.WG.FWG.C.EXPANDED, # Define the type of straight waveguide in automatic routing
        bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR, # Define the type of bend during automatic routing
        # Define the connection relationship between device ports in specs
        specs=[
            # Use >> to define connection relationships
            gc1["op_0"] >> fp.Waypoint(-50, -50, 0) >> gc4["op_0"],
            # Use LINKER to define the interconnection of the specified device port
            TECH.LINKER.SWG_WIRE_FWG_EULER(
                start=gc2["op_0"],
                end=gc5["op_0"],
                waypoints=[fp.Waypoint(0, 50, 0)]
            ),
            # Use LinkBetween to define a separate segment of the connection, and you can modify the type of the straight waveguide and bend with parameters.
            fp.LinkBetween(
                start=gc3["op_0"],
                end=gc6["op_0"],
                link_type=TECH.WG.SWG.C.EXPANDED,
                bend_factory=TECH.WG.SWG.C.WIRE.BEND_CIRCULAR,
                waypoints=[fp.Waypoint(50, 150, 0)]
            ),
        ],
    )
    # Add the devices returned by Linked to insts
    insts += device

.. image:: ../images/single2single.png


The differences between the two methods are:

1. ``LinkBetween`` requires setting the ``waveguide_type`` and ``bendfactory`` to define the waveguide and bend in the routing.

2. ``LINKER`` is already configured in the ``technology`` file, no need to define ``waveguide_type`` and ``bendfactory`` again.

Code details::

    from dataclasses import dataclass
    from fnpcell import all as fp
    from gpdk import all as pdk
    from gpdk.technology import get_technology, PCell

    @dataclass(eq=False)
    class Linked(PCell):
        def build(self):
            insts, elems, ports = super().build()
            TECH = get_technology()
            # fmt: off
            # call devices
            GC = pdk.GratingCoupler(waveguide_type=TECH.WG.FWG.C.WIRE)
            # Place the devices in different locations and add them to insts
            gc1 = GC.h_mirrored().translated(-100, -100)
            insts += gc1
            gc2 = GC.h_mirrored().translated(-100, 0)
            insts += gc2
            gc3 = GC.h_mirrored().translated(-100, 100)
            insts += gc3
            gc4 = GC.translated(100, -50)
            insts += gc4
            gc5 = GC.translated(100, 50)
            insts += gc5
            gc6 = GC.translated(100, 150)
            insts += gc6
            # Interconnecting device ports by calling the create_links method
            device = fp.create_links(
                link_type=TECH.WG.FWG.C.EXPANDED, # Define the type of straight waveguide in automatic routing
                bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR, # Define the type of bend during auto routing
                # Define the connection relationship between device ports in specs
                specs=[
                    # Use >> to define connection relationships
                    gc1["op_0"] >> fp.Waypoint(-50, -50, 0) >> gc4["op_0"],
                    # Use LINKER to define the interconnection of the specified device port
                    TECH.LINKER.SWG_WIRE_FWG_EULER(
                        start=gc2["op_0"],
                        end=gc5["op_0"],
                        waypoints=[fp.Waypoint(0, 50, 0)]
                    ),
                   # Use LinkBetween to define a separate segment of the connection, and you can modify the type of the straight waveguide and bend with parameters.
                    fp.LinkBetween(
                        start=gc3["op_0"],
                        end=gc6["op_0"],
                        link_type=TECH.WG.SWG.C.EXPANDED,
                        bend_factory=TECH.WG.SWG.C.WIRE.BEND_CIRCULAR,
                        waypoints=[fp.Waypoint(50, 150, 0)]
                    ),
                ],
            )
            # Add the devices returned by Linked to insts
            insts += device

            # fmt: on
            return insts, elems, ports

    if __name__ == "__main__":
        from pathlib import Path

        gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
        library = fp.Library()

        TECH = get_technology()
        # ================================================
        # fmt: off

        library += Linked()

        # fmt: on
        # ================================================
        fp.export_gds(library, file=gds_file)
        fp.plot(library)

See the comments section in the code for details
