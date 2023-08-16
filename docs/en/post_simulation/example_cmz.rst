Cascaded Mach-Zehnder (CMZ) wavelength filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example is to demonstrate how ``PhotoCAD`` post-simulation can be used in a CMZ wavelength filter [1]_ and help users to validate their concepts from a simple simulation implementation.

Wavelength Splitters
--------------------------

To demultiplex 8 wavelength channel, 3-level of wavelength splitters will be needed to implement in the CMZ circuit.

#. 1st level: two 50/50 DC.

   ::

        class DEMUX_1(fp.PCell):
            L_FSR_coeff: float = fp.PositiveFloatParam(default=1)
            L_shift_coeff: float = fp.NonNegFloatParam(default=0)
            FSR: float = 3.2  # nm
            lambda_center: float = 1490  # nm
            neff: float = 2.4
            ng: float = 4.0

            def build(self):
                insts, elems, ports = super().build()
                TECH = get_technology()
                FSR = self.FSR * 1e-9
                lambda_center = self.lambda_center * 1e-9
                neff = self.neff
                ng = self.ng
                L_FSR_coeff = self.L_FSR_coeff
                L_shift_coeff = self.L_shift_coeff

                base_length = 50  # um
                delta_L_base = (lambda_center**2 / 2 / FSR / ng) * 1e6
                delta_L_FS = (lambda_center / neff) * 1e6
                delta_L_FSR = delta_L_base / L_FSR_coeff
                delta_L_shift = delta_L_FS * L_shift_coeff
                delta_L = delta_L_FSR + delta_L_shift

                DC_050 = pdk.DC_050()

                DC1 = DC_050.translated(-60, 0)
                insts += DC1, "DC1"
                DC2 = DC_050.translated(0, 0)
                insts += DC2, "DC2"

                device = fp.create_links(
                    link_type=TECH.WG.FWG.C.WIRE,
                    bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR,
                    specs=[
                        fp.LinkBetween(
                            DC1["op_2"],
                            DC2["op_1"],
                            target_length=base_length,
                        ),
                        fp.LinkBetween(DC1["op_3"], DC2["op_0"], target_length=base_length + delta_L),
                    ],
                )
                insts += device

                ports += DC1["op_0"].with_name("op_1")
                ports += DC1["op_1"].with_name("op_2")
                ports += DC2["op_2"].with_name("op_3")
                ports += DC2["op_3"].with_name("op_4")

                # fmt: on
                return insts, elems, ports

            def sim_model(self, left_coupling: float = 0.5, right_coupling: float = 0.5):
                left_dc = self.get("DC1", pdk.DC_050)
                right_dc = self.get("DC2", pdk.DC_050)
                models = {
                    left_dc: left_dc.sim_model(coupling=left_coupling),
                    right_dc: right_dc.sim_model(coupling=right_coupling),
                }
                return fp.sim.CircuitModel(self, self.netlist(), models)

.. image:: ../images/1st_gds.png
.. image:: ../images/1st_sim.png

#. 2nd level: 50/50 DC, 71/29 DC, 92/8 DC.

   ::

        class DEMUX_2(fp.PCell):
            L_FSR_coeff: float = fp.PositiveFloatParam(default=1)
            L_shift_coeff: float = fp.NonNegFloatParam(default=0)
            FSR: float = 3.2  # nm
            lambda_center: float = 1490  # nm
            neff: float = 2.4
            ng: float = 4.0

            def build(self):
                insts, elems, ports = super().build()
                TECH = get_technology()
                FSR = self.FSR * 1e-9
                lambda_center = self.lambda_center * 1e-9
                neff = self.neff
                ng = self.ng
                L_FSR_coeff = self.L_FSR_coeff
                L_shift_coeff = self.L_shift_coeff

                base_length = 50
                delta_L_base = (lambda_center**2 / 2 / FSR / ng) * 1e6
                delta_L_FS = (lambda_center / neff) * 1e6
                delta_L_FSR = delta_L_base / L_FSR_coeff
                delta_L_shift = delta_L_FS * L_shift_coeff
                delta_L = delta_L_FSR + delta_L_shift

                DC_050 = pdk.DC_050()
                DC_029 = pdk.DC_029()
                DC_008 = pdk.DC_008()

                DC1 = DC_050.translated(-95, 0)
                insts += DC1, "DC1"
                DC2 = DC_029.translated(-40, 0)
                insts += DC2, "DC2"
                DC3 = DC_008.translated(0, 0)
                insts += DC3, "DC3"

                device = fp.create_links(
                    link_type=TECH.WG.FWG.C.WIRE,
                    bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR,
                    specs=[
                        fp.LinkBetween(
                            DC1["op_2"],
                            DC2["op_1"],
                            target_length=base_length,
                        ),
                        fp.LinkBetween(DC1["op_3"], DC2["op_0"], target_length=base_length + delta_L),
                        fp.LinkBetween(DC2["op_2"], DC3["op_1"], target_length=base_length + 2 * delta_L),
                        fp.LinkBetween(DC2["op_3"], DC3["op_0"], target_length=base_length),
                    ],
                )
                insts += device

                ports += DC1["op_0"].with_name("op_1")
                ports += DC1["op_1"].with_name("op_2")
                ports += DC3["op_2"].with_name("op_3")
                ports += DC3["op_3"].with_name("op_4")

                # fmt: on
                return insts, elems, ports

            def sim_model(self, left_coupling: float = 0.5, mid_coupling: float = 0.29, right_coupling: float = 0.08):
                left_dc = self.get("DC1", pdk.DC_050)
                mid_dc = self.get("DC2", pdk.DC_029)
                right_dc = self.get("DC3", pdk.DC_008)
                models = {
                    left_dc: left_dc.sim_model(coupling=left_coupling),
                    mid_dc: mid_dc.sim_model(coupling=mid_coupling),
                    right_dc: right_dc.sim_model(coupling=right_coupling),
                }
                return fp.sim.CircuitModel(self, self.netlist(), models)


.. image:: ../images/2st_gds.png
.. image:: ../images/2st_sim.png

#. 3rd level: 50/50 DC, 71/29 DC, 92/8 DC.

   ::

        class DEMUX_3(fp.PCell):
            L_FSR_coeff: float = fp.PositiveFloatParam(default=1)
            L_shift_coeff: float = fp.NonNegFloatParam(default=0)
            FSR: float = 3.2  # nm
            lambda_center: float = 1490  # nm
            # wl_offset: float = 0
            neff: float = 2.4
            ng: float = 4.0

            def build(self):
                insts, elems, ports = super().build()
                TECH = get_technology()
                FSR = self.FSR * 1e-9
                lambda_center = self.lambda_center * 1e-9
                neff = self.neff
                ng = self.ng
                L_FSR_coeff = self.L_FSR_coeff
                L_shift_coeff = self.L_shift_coeff

                base_length = 50
                delta_L_base = (lambda_center**2 / 2 / FSR / ng) * 1e6
                delta_L_FS = (lambda_center / neff) * 1e6
                delta_L_FSR = delta_L_base / L_FSR_coeff
                delta_L_shift = delta_L_FS * L_shift_coeff

                delta_L = delta_L_FSR + delta_L_shift
                Lpi = (lambda_center / (2 * neff)) * 1e6

                DC_050 = pdk.DC_050()
                DC_020 = pdk.DC_020()
                DC_004 = pdk.DC_004()

                DC1 = DC_050.translated(-97.5, 0)
                insts += DC1, "DC1"
                DC2 = DC_020.translated(-45, 0)
                insts += DC2, "DC2"
                DC3 = DC_020.translated(0, 0)
                insts += DC3, "DC3"
                DC4 = DC_004.translated(36, 0)
                insts += DC4, "DC4"

                device = fp.create_links(
                    link_type=TECH.WG.FWG.C.WIRE,
                    bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR,
                    specs=[
                        fp.LinkBetween(
                            DC1["op_2"],
                            DC2["op_1"],
                            target_length=base_length,
                        ),
                        fp.LinkBetween(DC1["op_3"], DC2["op_0"], target_length=base_length + delta_L),
                        fp.LinkBetween(DC2["op_2"], DC3["op_1"], target_length=base_length + 2 * delta_L),
                        fp.LinkBetween(DC2["op_3"], DC3["op_0"], target_length=base_length),
                        fp.LinkBetween(DC3["op_2"], DC4["op_1"], target_length=base_length + 2 * delta_L + Lpi),
                        fp.LinkBetween(DC3["op_3"], DC4["op_0"], target_length=base_length),
                    ],
                )
                insts += device

                ports += DC1["op_0"].with_name("op_1")
                ports += DC1["op_1"].with_name("op_2")
                ports += DC4["op_2"].with_name("op_3")
                ports += DC4["op_3"].with_name("op_4")

                # fmt: on
                return insts, elems, ports

            def sim_model(self, left_coupling: float = 0.5, mid_coupling: float = 0.20, mid2_coupling: float = 0.20, right_coupling: float = 0.04):
                left_dc = self.get("DC1", pdk.DC_050)
                mid_dc = self.get("DC2", pdk.DC_020)
                mid2_dc = self.get("DC3", pdk.DC_020)
                right_dc = self.get("DC4", pdk.DC_004)
                models = {
                    left_dc: left_dc.sim_model(coupling=left_coupling),
                    mid_dc: mid_dc.sim_model(coupling=mid_coupling),
                    mid2_dc: mid2_dc.sim_model(coupling=mid2_coupling),
                    right_dc: right_dc.sim_model(coupling=right_coupling),
                }
                return fp.sim.CircuitModel(self, self.netlist(), models)


.. image:: ../images/3st_gds.png
.. image:: ../images/3st_sim.png

CMZ wavelength filter
------------------------------











.. [1] Horst, F., Green, W. M., Assefa, S., Shank, S. M., Vlasov, Y. A., & Offrein, B. J. (2013). Cascaded Mach-Zehnder wavelength filters in silicon photonics for low loss and flat pass-band WDM (de-)multiplexing. Optics express, 21(10), 11652–11658.