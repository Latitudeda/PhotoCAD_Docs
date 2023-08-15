
Component level simulation model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Important note: To run the below simulation models in PhotoCAD, upgrades to fnpcell-1.5.1 and sflow-0.8.36 are required**

In this section, we will introduce a method for users to write their own S-Matrix for their components. Here we use the simplest waveguide model as an example.

WGModel class
----------------------

 ::

    from typing import Any, Sequence, Tuple

    from fnpcell import all as fp
    import numpy as np
    from fnpcell.interfaces import IScatterMatrix
    from fnpcell.interfaces import angle_between, distance_between
    from gpdk.technology import get_technology


    class WGModel(fp.sim.SimModel):
        op_0: fp.IOwnedPort
        op_1: fp.IOwnedPort
        wl0: float = 1.49
        neff: float = 2.4
        ng: float = 4.0
        loss: float = 0.0

        def simulate_scatter(self, wavelengths: Sequence[float]) -> IScatterMatrix:
            wl = np.array(wavelengths)
            wl0 = np.array(self.wl0)
            neff = np.array(self.neff)
            ng = np.array(self.ng)
            loss = np.array(self.loss)
            length = fp.distance_between(self.op_0.position, self.op_1.position)

            dwl = wl - self.wl0
            dneff_dwl = (ng - neff) / wl0
            neff = neff - dwl * dneff_dwl

            mag = 10 ** (-loss * length / 20)
            arg = 2 * np.pi * neff * length / wl

            op_0 = self.op_0
            op_1 = self.op_1

            S = fp.sim.SMatrix()

            S[op_1, op_0] = S[op_0, op_1] = mag, arg

            return S

Script description
---------------------------------
* Import functions and modules

  ::

    from typing import Any, Sequence, Tuple

    from fnpcell import all as fp
    import numpy as np
    from fnpcell.interfaces import IScatterMatrix
    from fnpcell.interfaces import angle_between, distance_between
    from gpdk.technology import get_technology

* List the ports and parameters that will be implemented in this simulation model.

 ::

        op_0: fp.IOwnedPort
        op_1: fp.IOwnedPort
        wl0: float = 1.49
        neff: float = 2.4
        ng: float = 4.0
        loss: float = 0.0

* Define the S-Matrix by calculating the magnitude and argument relation between two ports.

  ``fp.sim.SMatrix()`` is where the magnitude and argument should be assigned.

 ::

        def simulate_scatter(self, wavelengths: Sequence[float]) -> IScatterMatrix:
            wl = np.array(wavelengths)
            wl0 = np.array(self.wl0)
            neff = np.array(self.neff)
            ng = np.array(self.ng)
            loss = np.array(self.loss)
            length = fp.distance_between(self.op_0.position, self.op_1.position)

            dwl = wl - self.wl0
            dneff_dwl = (ng - neff) / wl0
            neff = neff - dwl * dneff_dwl

            mag = 10 ** (-loss * length / 20)
            arg = 2 * np.pi * neff * length / wl

            op_0 = self.op_0
            op_1 = self.op_1

            S = fp.sim.SMatrix()

            S[op_1, op_0] = S[op_0, op_1] = mag, arg

            return S

Other simulation models
-----------------------------------

* Directional Coupler

 ::

        class DCModel(fp.sim.SimModel):
            op_0: fp.IOwnedPort
            op_1: fp.IOwnedPort
            op_2: fp.IOwnedPort
            op_3: fp.IOwnedPort
            coupling: float = 0.5

            def simulate_scatter(self, wavelengths: Sequence[float]) -> IScatterMatrix:
                coupling = np.array(self.coupling)
                kappa = coupling**0.5
                tau = (1 - coupling) ** 0.5

                op_0, op_1, op_2, op_3 = self.op_0, self.op_1, self.op_2, self.op_3

                S = fp.sim.SMatrix()

                S[op_2, op_1] = S[op_1, op_2] = tau, 0
                S[op_3, op_1] = S[op_1, op_3] = kappa, np.pi / 2
                S[op_2, op_0] = S[op_0, op_2] = kappa, np.pi / 2
                S[op_3, op_0] = S[op_0, op_3] = tau, 0

                return S

* Grating Coupler

 ::

        def simulate_scatter(self, wavelengths: Sequence[float]) -> IScatterMatrix:
        wl = np.array(wavelengths)
        wl0 = np.array(self.wl0)
        peak_transmission = np.array(self.peak_transmission)
        bandwidth = np.array(self.bandwidth)

        sigma = bandwidth / 2.35482

        mag = ((peak_transmission ** 0.5) * np.exp(-(wl-wl0) ** 2.0 /( 2.0 * (sigma ** 2.0))))
        arg = 2 * np.pi * 2.4 / wl

        op_0 = self.op_0
        op_1 = self.op_1

        S = fp.sim.SMatrix()

        S[op_1, op_0] = S[op_0, op_1] = mag, arg

        return S

Summary
-----------------------------------

The simulation model mentioned above will be converted into their corresponding S-parameter matrices, and these matrices will be cascaded for simulating multiple components.

It is important to note that if the model sampling point of a device differs from the sampling point set during the link simulation, the engine will use linear interpolation to ensure consistency between the model sampling point of each device and the sampling point set during the link simulation.
