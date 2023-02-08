``wg.py`` configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure arrays of theoretical parameters corresponding to different waveguide types in ``wg.py``, with ``wl`` , ``neff`` , ``loss`` , and define ``theoretical_parameters`` function to associate arrays with waveguide types. Note that, this will make it possible to call the theoretical parameters of the current waveguide type when modeling a component, if you already have some way to obtain the theoretical parameters(External file, Self-built S-matrix) then you do not need to do these configurations.

#. Step1:

   The arrays are defined in ``gpdk`` > ``technology`` > ``wg.py``, below listed one of the example::

        FWG_C_WIRE_SIM_WL = [1.4, 1.5, 1.6]
        FWG_C_WIRE_SIM_NEFF = [2.5066666, 2.4, 2.2933333]
        FWG_C_WIRE_SIM_LOSS = [1, 1, 1]

   Note that the wavelength unit is um, loss unit is dB/cm, and the three array lengths need to be consistent.

#. Step2:

   Define the theoretical parameters under the specific class by entering the three arrays defined above into``fpt.sim.TheoreticalParameters`` and return::

        @fpt.const_property
        def theoretical_parameters(self):
            if self == WG.FWG.C.WIRE:
                return fpt.sim.TheoreticalParameters(wl=FWG_C_WIRE_SIM_WL, n_eff=FWG_C_WIRE_SIM_NEFF, loss=FWG_C_WIRE_SIM_LOSS)
            raise NotImplementedError( "No theoretical parameters for this updated waveguide type")

   The error message is to make waveguide type judgement, which means only when the current waveguide matches ``FWG.C.WIRE`` then return the theoretical parameters defined above.