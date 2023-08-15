``wg.py`` configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To configure arrays of theoretical parameters for different waveguide types in ``wg.py``, define variables for wavelength (``wl``), effective refractive index (``neff``), and loss (``loss``) for each waveguide type, and create a function called ``theoretical_parameters`` to associate these variables with their respective waveguide types. This will allow for the easy retrieval of theoretical parameters for the current waveguide type during component modeling. Note that if you already have a way to obtain the theoretical parameters (e.g. from an external file or self-built S-matrix), you do not need to perform these configurations.

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