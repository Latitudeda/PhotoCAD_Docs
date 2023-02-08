
Types of simulation model commonly used in **PhotoCAD**
----------------------------------------------------------------

**Important note: To run the below simulation models in PhotoCAD, upgrades to fnpcell-1.5.1 and sflow-0.8.36 are required**

Below table lists four commonly used simulation model. To simulate the circuit, users have to define ``sim_model`` function to set the link simulation model for a component, either based on an S-parameter file(e.g. MMI1x2) or based on the behavior described by some formula(e.g. Straight waveguide, Taper).

``SMatrixWavelengthModel()`` and ``ExternalFileModel()`` can cover full-components models. ``StraightWaveguideModel()`` and ``TaperLinearModel()`` serve a single device as exceptions.


+---------------------------------+-------------------------------------------------------------------+------------------------------------------------+
|                                 | The parameters that need to be entered                            | Remark                                         |
+=================================+===================================================================+================================================+
| fp.sim.SMatrixWavelengthModel() | 1. S-matrix;                                                      | Metadata for the ports of symbol in schematic. |
|                                 | 2. The wavelength range corresponding to the S-matrix;            |                                                |
|                                 | 3. Metadata(optional)                                             |                                                |
+---------------------------------+-------------------------------------------------------------------+------------------------------------------------+
| fp.sim.ExternalFileModel()      | -parameter file path                                              | Only support file with suffix “dat” right now. |
+---------------------------------+-------------------------------------------------------------------+------------------------------------------------+
| fp.sim.StraightWaveguideModel() | 1. Length of waveguide;                                           | Only for straight waveguide                    |
|                                 | 2. The theoretical parameters corresponding to the waveguide type |                                                |
+---------------------------------+-------------------------------------------------------------------+------------------------------------------------+
| fp.sim.TaperLinearModel()       | 1. Length of taper;                                               | Only for linear taper                          |
|                                 | 2. The theoretical parameters corresponding to the two port types |                                                |
+---------------------------------+-------------------------------------------------------------------+------------------------------------------------+

``SMatrixWavelengthModel``
--------------------------------------------
``SMatrixWavelengthModel`` creates a user-defined S-matrix and send the S-parameter to the simulation model, simulation parameters such as wavelength, effective index, propagation loss, temperature can be added in the model. ``gpdk`` > ``components`` > ``straight`` > ``straight.py`` shows an example of defining ````SMatrixWavelengthModel`` in a straight waveguide.


#. Define the simulation model in ``Straight`` and import necessary module::

        @fp.cache()
        def sim_model(self, env: fp.ISimEnv):
            import numpy as np

#. Get the defined ports from the component and set the length used below in meter::

        op_0, op_1 = self["op_0"], self["op_1"]
        length = self.length * 1e-6

#. Get the ``theoretical_parameters`` from ``waveguide_type``, details are shown in (:doc:`theoretical_parameters`)::

        params = fp.sim.TheoreticalParameters(self.waveguide_type.theoretical_parameters)
            wl = np.asanyarray(params.wl) * 1e-6  # wavelength in um => m
            n_eff = np.asanyarray(params.n_eff)
            loss = np.asanyarray(params.loss) * 1e2  # loss in dB/cm => dB/m

    Users are also allowed to build theoretical parameters by your custom functions::

        n_eff = func_a(wl, waveguide_type, T)
        loss = func_b(wl, waveguide_type, T)

#. External parameters can be created by ``env`` and get them for interpolation::

        wavelength = np.asanyarray(env.wavelength) * 1e-6  # wavelength in um => m
        T = env["T"]

#. Setup some calculations from these above parameters for further use::

        mag = 10 ** (-loss * length / 20)
        arg = 2 * np.pi * n_eff * length / wl

#. Get the empty S matrix and assign the value::

        S = fp.sim.SMatrix()
        S[op_1, op_0] = S[op_0, op_1] = mag, arg

   Polarization rotation is also supported in the S-matrix model sinulation::

        S = fp.sim.Smatrix(allow_polarization_rotation=True)
        S[op_1[“TE”], op_0[“TM”]] = mag, arg

#. Add metadata if needed and return ``SMatrixWavelengthModel``::

        metadata = {
            "ports": {
                op_0.name: "LEFT",
                op_1.name: "RIGHT",
            }
        }
        return fp.sim.SMatrixWavelengthModel(wl, S, metadata=metadata)





``ExternalFileModel``
--------------------------------------------

``ExternalFileModel`` allows users to generate simulation model based on their S-parameter data. Users define the path of the S-parameter file and pass the path to ``fp.sim.ExternalFileModel()``, then **PhotoCAS** will find the file and parse it when running the simulation. Note that, file format has to be ``.dat`` to be recognized by **PhotoCAD**.

#. S-parameter file format

   **PhotoCAD** only supports ``.dat`` file, which includes the below text(extract from ``gpdk`` > ``components`` > ``mmi`` > ``Mmi1x2.dat``):

   * The ports name and the reference position of the port in the schematic, the ports name needs to be consistent with the port name in PCell::

        ["op_0","LEFT"]
        ["op_1","RIGHT"]
        ["op_2","RIGHT"]

   * ``output port``, mode label, ``output mode``, ``input port``, ``input mode``, type::

        ("op_0","mode 1",1,"op_0",1,"transmission")

   * Frequency, |S|, arg(S)::

        1.9156067603833869e+14 2.7442972188120671e-02 -6.4430396820656299e-01
        1.9156506253180034e+14 2.7351617044051896e-02 -6.3548125587455162e-01
        1.9156944902526200e+14 2.7260363112957844e-02 -6.2664416544812684e-01
        1.9157383551872366e+14 2.7169214678454557e-02 -6.1779257455545133e-01
        1.9157822201218531e+14 2.7078176028702078e-02 -6.0892636075894513e-01
        ...

#. Example::

        @dataclass(eq=False)
        class BendCircular90_FWG_C_EXPANDED(BendCircular, locked=True):
            radius: float = fp.PositiveFloatParam(default=3.4, doc="Bend radius")
            waveguide_type: fp.IWaveguideType = fp.WaveguideTypeParam()

            def _default_waveguide_type(self):
                return get_technology().WG.FWG.C.EXPANDED

            @fp.cache()
            def sim_model(self, env: fp.ISimEnv):

                file_path = Path("BendCircular90_radius=10").with_suffix(".dat")

                return fp.sim.ExternalFileModel(file_path)


Specific component simulation model
-----------------------------------
#. ``StraightWaveguideModel``: In this function, it will automatically calculate the phase and amplitude changes according to the theoretical parameters and the current waveguide length then build the simulation model which is only suitable for ``Straight``. The theoretical parameters are defined in ``wg.py`` in advance.

   Example(check out the full code: ``gpdk`` > ``components`` > ``straight`` > ``straight.py``) ::

        @fp.cache()
        def sim_model(self, env: fp.ISimEnv):
            return fp.sim.StraightWaveguideModel(self.waveguide_type.theoretical_parameters, length=self.length)

#. ``TaperLinearModel``: In this function, two theoretical parameters( ``left_type`` and ``right_type`` ) will first been averaged. Then it will automatically calculate the phase and amplitude changes according to the averaged theoretical parameters and the current Taper length then build the simulation model which is only suitable for ``Taper``.

   Example(check out the full code: ``gpdk`` > ``components`` > ``taper`` > ``taper_linear.py``) ::

        @fp.cache()
        def sim_model(self, env: fp.ISimEnv):
            left_model = self.left_type.theoretical_parameters
            right_model = self.right_type.theoretical_parameters
            return fp.sim.TaperLinearModel([left_model, right_model], length=self.length)


Summary
-----------------------------------

The above four types of device models will be converted into the S-parameter matrix of the corresponding component, and the S-parameter matrix of multiple components will be cascaded to obtain simulation results when running simulation.

It should be noted that when the model sampling point of the device is different from the sampling point set during the link simulation, the engine will perform linear interpolation based on the model of the device to ensure that the model sampling point of each device is consistent with the sampling point set during the link simulation.













