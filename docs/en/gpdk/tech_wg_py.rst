.. _wg.py :

wg.py
============================================================

The file mainly defines various waveguide types and their corresponding configurations such as width, simulation parameters.

waveguide configuration
--------------------------------
In **gpdk**, three types of waveguides are defined, which are ``FWG``, ``MWG``, and ``SWG``.

Each waveguide type will then create different band type based on the chosen band ( ``C-band``, ``O-band`` ), and beyond each band type, 4 other types depends on the waveguide linewidth are generated ( ``WIRE``, ``WIRE_TETM``, ``EXPANDED``, ``EXPANDED_TETM`` ).

O-band can be adjusted by ``O_BAND_RATIO = 0.8``, ``TETM`` and ``EXPANDED`` can also be adjusted by ``WIRE_TETM_RATIO`` and ``EXPANDED_TETM_RATIO``, so that the users don't need to define every function.

First, we define the width of every waveguides that will be consider as a parameter and be send to each waveguide class.

::

    FWG_C_WIRE_WIDTH = 0.45
    FWG_C_EXPANDED_WIDTH = 0.8
    FWG_C_TRENCH_WIDTH = 2.0

    MWG_C_WIRE_WIDTH = 1
    MWG_C_EXPANDED_WIDTH = 1.5
    MWG_C_TRENCH_WIDTH = 5.0

    SWG_C_WIRE_WIDTH = 1.0
    SWG_C_EXPANDED_WIDTH = 1.5
    SWG_C_TRENCH_WIDTH = 5.0

    WIRE_TETM_RATIO = 1.2
    EXPANDED_TETM_RATIO = 2.0

    O_BAND_RATIO = 0.8

Define parameters in each waveguide types
-------------------------------------------

The information of each waveguide type are then defined in each waveguide class, such as critical dimension bias, layer information.

The structure of each waveguide is build in ``technology > interfaces > wg.py``, we can create a waveguide class (FWG_C) that inherits from the waveguide interface ``CoreCladdingWaveguideType`` which defines the structure of the waveguide type with one core layer and one cladding layer, including the profile, waveguide width, etc.

Since there could be many waveguide types (``FWG_C``, ``FWG_O``, ``MWG_C``, etc.) using the same waveguide interface (``CoreCladdingWaveguideType``), we then assign different parameters(CD bias, band, core/cladding layer) to those waveguide types in each class.

::

        @fpt.hash_code
        class FWG_C(CoreCladdingWaveguideType):
            @fpt.const_property
            def core_bias(self):
                return fpt.CDBiasLinear(0.1)

            @fpt.const_property
            def cladding_bias(self):
                return fpt.CDBiasLinear(0)

            @fpt.const_property
            def band(self):
                from gpdk.technology import get_technology

                return get_technology().BAND.C

            @fpt.const_property
            def core_layer(self):
                from gpdk.technology import get_technology

                return get_technology().LAYER.FWG_COR

            @fpt.const_property
            def cladding_layer(self):
                from gpdk.technology import get_technology

                return get_technology().LAYER.FWG_CLD

            @fpt.const_property
            def straight_factory(self):
                return StraightFactory()


        @fpt.hash_code
        class FWG_O(CoreCladdingWaveguideType):



        @fpt.hash_code
        class MWG_C(CoreCladdingWaveguideType):



Generate waveguide class
-------------------------------------
In this section, we used the class generated above as a parent class to create every waveguide class which parameters are defined in the above section. The bend factories of each specific waveguide are also defined in this section.
::

        class WG:
            class FWG:
                class C(FWG_C):
                    @fpt.staticconst
                    def WIRE():
                        class WIRE(__class__):
                            core_design_width: float = FWG_C_WIRE_WIDTH
                            cladding_design_width: float = FWG_C_WIRE_WIDTH + FWG_C_TRENCH_WIDTH * 2

                            @fpt.const_property
                            def bend_factory(self):
                                return self.BEND_EULER


                            @fpt.const_property
                            def BEND_CIRCULAR(self):
                                return CircularBendFactory(radius_eff=self.cladding_width / 2 + 1, waveguide_type=self)

                            @fpt.const_property
                            def BEND_EULER(self):
                                return EulerBendFactory(radius_min=self.cladding_width / 2 + 1, l_max=5, waveguide_type=self)

                        return WIRE()

                    @fpt.staticconst
                    def WIRE_TETM():

                        return WIRE_TETM()

                    @fpt.staticconst
                    def EXPANDED():

                        return EXPANDED()

                    @fpt.staticconst
                    def EXPANDED_TETM():

                        return EXPANDED_TETM()

                class O(FWG_O):

            class MWG:
                class C(MWG_C):

                class O(MWG_O):

Generate wg information to csv file
---------------------------------------------
The above information of each waveguides will be export to a csv file, which stored under ``generated`` file. This allows users to check the information of each waveguide, including waveguide width, radius of each bend waveguide, and the port names.
::

    if __name__ == "__main__":
        from pathlib import Path
        from fnpcell import all as fp
        from gpdk.technology import get_technology

        TECH = get_technology()
        folder = Path(__file__).parent
        generated_folder = folder / "generated"
        csv_file = generated_folder / "wg.csv"
        # ================================

        fp.util.generate_csv_from_waveguides(csv_file=csv_file, waveguides=TECH.WG, overwrite=True)

The final generated csv

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NAME                              | CONFIGURATION                                                                                                                                                                                      |
+===================================+====================================================================================================================================================================================================+
| FWG.C.WIRE                        | core_layout_width=0.55, cladding_layout_width=4.45,   core_design_width=0.45, cladding_design_width=4.45, port_names=('op_0',   'op_1')                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.WIRE.BEND_CIRCULAR          | radius_eff=3.225                                                                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.WIRE.BEND_EULER             | radius_min=3.225, l_max=5                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED                    | core_layout_width=0.9, cladding_layout_width=4.8, core_design_width=0.8,   cladding_design_width=4.8, port_names=('op_0', 'op_1')                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED.BEND_CIRCULAR      | radius_eff=3.4                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED.BEND_EULER         | radius_min=3.4, l_max=10                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED_TETM               | core_layout_width=1.7000000000000002, cladding_layout_width=5.6,   core_design_width=1.6, cladding_design_width=5.6, port_names=('op_0', 'op_1')                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED_TETM.BEND_CIRCULAR | radius_eff=3.8                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.EXPANDED_TETM.BEND_EULER    | radius_min=3.8, l_max=10                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.WIRE_TETM                   | core_layout_width=0.64, cladding_layout_width=4.54,   core_design_width=0.54, cladding_design_width=4.54, port_names=('op_0',   'op_1')                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.WIRE_TETM.BEND_CIRCULAR     | radius_eff=10                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.C.WIRE_TETM.BEND_EULER        | radius_min=3.27, l_max=5                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.O.WIRE                        | core_layout_width=0.4600000000000001,   cladding_layout_width=3.5600000000000005,   core_design_width=0.36000000000000004,   cladding_design_width=3.5600000000000005, port_names=('op_0', 'op_1') |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.O.EXPANDED                    | core_layout_width=0.7400000000000001, cladding_layout_width=3.84,   core_design_width=0.6400000000000001, cladding_design_width=3.84,   port_names=('op_0', 'op_1')                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.O.EXPANDED_TETM               | core_layout_width=1.3800000000000003,   cladding_layout_width=4.4799999999999995,   core_design_width=1.2800000000000002,   cladding_design_width=4.4799999999999995, port_names=('op_0', 'op_1')  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FWG.O.WIRE_TETM                   | core_layout_width=0.532, cladding_layout_width=3.632,   core_design_width=0.43200000000000005, cladding_design_width=3.632,   port_names=('op_0', 'op_1')                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE                        | core_layout_width=1.15, cladding_layout_width=11.0, core_design_width=1,   cladding_design_width=11.0, port_names=('op_0', 'op_1')                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE.BEND_CIRCULAR          | radius_eff=6.5                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE.BEND_EULER             | radius_min=6.5, l_max=15                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED                    | core_layout_width=1.65, cladding_layout_width=11.5,   core_design_width=1.5, cladding_design_width=11.5, port_names=('op_0',   'op_1')                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED.BEND_CIRCULAR      | radius_eff=6.75                                                                                                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED.BEND_EULER         | radius_min=6.75, l_max=25                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED_TETM               | core_layout_width=3.15, cladding_layout_width=13.0,   core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0',   'op_1')                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED_TETM.BEND_CIRCULAR | radius_eff=7.5                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.EXPANDED_TETM.BEND_EULER    | radius_min=7.5, l_max=25                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE_TETM                   | core_layout_width=1.3499999999999999, cladding_layout_width=11.2,   core_design_width=1.2, cladding_design_width=11.2, port_names=('op_0',   'op_1')                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE_TETM.BEND_CIRCULAR     | radius_eff=6.6                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.C.WIRE_TETM.BEND_EULER        | radius_min=6.6, l_max=15                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.O.WIRE                        | core_layout_width=0.9500000000000001, cladding_layout_width=8.8,   core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0', 'op_1')                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.O.EXPANDED                    | core_layout_width=1.35, cladding_layout_width=9.200000000000001,   core_design_width=1.2000000000000002,   cladding_design_width=9.200000000000001, port_names=('op_0', 'op_1')                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.O.EXPANDED_TETM               | core_layout_width=2.5500000000000003, cladding_layout_width=10.4,   core_design_width=2.4000000000000004, cladding_design_width=10.4,   port_names=('op_0', 'op_1')                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MWG.O.WIRE_TETM                   | core_layout_width=1.1099999999999999,   cladding_layout_width=8.959999999999999, core_design_width=0.96,   cladding_design_width=8.959999999999999, port_names=('op_0', 'op_1')                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SLOT.C.WIRE                       | core_layout_width=1.15, slot_layout_width=0.3,   cladding_layout_width=11.0, core_design_width=1.0, slot_design_width=0.3,   cladding_design_width=11.0, port_names=('op_0', 'op_1')               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SLOT.O.WIRE                       | core_layout_width=0.9500000000000001, slot_layout_width=0.24,   cladding_layout_width=8.8, core_design_width=0.8, slot_design_width=0.24,   cladding_design_width=8.8, port_names=('op_0', 'op_1') |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE                        | core_layout_width=1.15, cladding_layout_width=11.0,   core_design_width=1.0, cladding_design_width=11.0, port_names=('op_0',   'op_1')                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE.BEND_CIRCULAR          | radius_eff=6.5                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE.BEND_EULER             | radius_min=6.5, l_max=15                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED                    | core_layout_width=3.15, cladding_layout_width=13.0,   core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0',   'op_1')                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED.BEND_CIRCULAR      | radius_eff=7.5                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED.BEND_EULER         | radius_min=7.5, l_max=25                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED_TETM               | core_layout_width=3.15, cladding_layout_width=13.0,   core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0',   'op_1')                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED_TETM.BEND_CIRCULAR | radius_eff=7.5                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.EXPANDED_TETM.BEND_EULER    | radius_min=7.5, l_max=25                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE_TETM                   | core_layout_width=1.3499999999999999, cladding_layout_width=11.2,   core_design_width=1.2, cladding_design_width=11.2, port_names=('op_0',   'op_1')                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE_TETM.BEND_CIRCULAR     | radius_eff=6.6                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.C.WIRE_TETM.BEND_EULER        | radius_min=6.6, l_max=15                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.O.WIRE                        | core_layout_width=0.9500000000000001, cladding_layout_width=8.8,   core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0', 'op_1')                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.O.EXPANDED                    | core_layout_width=1.35, cladding_layout_width=9.200000000000001,   core_design_width=1.2000000000000002,   cladding_design_width=9.200000000000001, port_names=('op_0', 'op_1')                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.O.EXPANDED_TETM               | core_layout_width=2.5500000000000003, cladding_layout_width=10.4,   core_design_width=2.4000000000000004, cladding_design_width=10.4,   port_names=('op_0', 'op_1')                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWG.O.WIRE_TETM                   | core_layout_width=1.1099999999999999,   cladding_layout_width=8.959999999999999, core_design_width=0.96,   cladding_design_width=8.959999999999999, port_names=('op_0', 'op_1')                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWGR.C.WIRE                       | core_layout_width=1.15, cladding_layout_width=11.0,   core_design_width=1.0, cladding_design_width=11.0, port_names=('op_0',   'op_1'), period=1.0, duty_cycle=0.5                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SWGR.O.WIRE                       | core_layout_width=0.9500000000000001, cladding_layout_width=8.8,   core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0',   'op_1'), period=1.0, duty_cycle=0.5                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
