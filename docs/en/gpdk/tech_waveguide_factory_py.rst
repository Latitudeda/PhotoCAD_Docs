.. _waveguide_factory.py :


waveguide factory.py
============================================================

This script mainly provides a more intelligent solution for implementing port acquisition and bend routing in automatic waveguide routing. The main components are

 * Straight_
 * CircularBend_
 * Implementation_

Straight
---------------------------

Define class ``StraightFactory`` ::

    @dataclass(frozen=True)
    class StraightFactory(fpt.IStraightWaveguideFactory):
        def __call__(self, type: fpt.IWaveguideType, length: float):
            from gpdk.components.straight.straight import Straight

            straight = Straight(length=length, waveguide_type=type)
            return straight, ("op_0", "op_1")

Returns straight waveguide in ``gpdk > components > straight > Straight`` and port information to provide support for port connections during automatic routing.

CircularBend
---------------------------

Define class ``CircularBendFactory``::

    @dataclass(frozen=True)
    class CircularBendFactory(fpt.IBendWaveguideFactory):
        radius_eff: float
        waveguide_type: fpt.IWaveguideType = field(repr=False, compare=False)

        def __call__(self, central_angle: float):
            from gpdk.components.bend.bend_circular import BendCircular, BendCircular90_FWG_C_WIRE, BendCircular90_FWG_C_EXPANDED
            from gpdk.technology import get_technology

            TECH = get_technology()

            radius_eff = self.radius_eff
            bend = None
            if fp.is_close(abs(central_angle), math.pi / 2):
                if self.waveguide_type == TECH.WG.FWG.C.WIRE:
                    bend = BendCircular90_FWG_C_WIRE()
                elif self.waveguide_type == TECH.WG.FWG.C.EXPANDED:
                    bend = BendCircular90_FWG_C_EXPANDED()

                if bend and central_angle < 0:
                    bend = bend.v_mirrored()

            if bend is None:
                bend = BendCircular(degrees=math.degrees(central_angle), radius=radius_eff, waveguide_type=self.waveguide_type)

            return bend, radius_eff, ("op_0", "op_1")

The parameters of the ``CircularBendFactory`` that can be set optionally are

- radius_eff 
- waveguide_type

There are two options to apply this bend factory to waveguide routing.

- Assign ``CircularBendFactory(waveguide_type=waveguide_type, radius_eff=radius_eff)`` to the parameter ``bend_factory`` in the routing function e.g., ``Linked``, ``create_links`` and ``LinkBetween``.
- Implement ``CircularBendFactory`` to each waveguide class (please see :ref:`wg.py`) and set ``TECH.WG.FWG.C.WIRE.BEND_CIRCULAR`` once you've return ``CircularBendFactory`` to ``BEND_CIRCULAR`` under the class ``WG.FWG.C.WIRE``.

By giving a certain condition (certain waveguide type and certain bending angle, TECH.WG.FWG.C.WIRE and 90 degree bend for example), users are allowed to assign a fixed bend (either a GDS import cell or fixed cell) to this waveguide type.

This means that when the bend angle is 90 degree and the waveguide type of two connected ports are also ``FWG.C.WIRE``, ``BendCircular90_FWG_C_WIRE`` will be automatically use.


Implementation
---------------------------
There are two ways to implement ``waveguide_factory`` for further use, one is to set it as default for every waveguide type, and another is to define a ``waveguide_factory`` by themselves and use it for auto-routing.

* Set as default in ``wg.py``

  Here we use the class named ``CircularBendFactory`` which we just defined. You can set ``radius_eff`` parameter to a value according to the technical specifications. We recommend that implementing ``bend_factory`` for every ``waveguide_type`` that you created so that you can set up several types of ``bend_factory`` as units in routing function.

  ``straight_factory`` and ``bend_factory`` are defined in ``wg.py`` to automatically use the PCell of ``straight`` and ``bend`` in the routing.


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



* Manually define ``bend_factory``

  Below scripts show how to generate a user-defined ``bend_factory``.

  ::

    @dataclass(frozen=True)
    class user_defined_bendfactory(fpt.IBendWaveguideFactory):
        radius_eff: float
        waveguide_type: fpt.IWaveguideType = field(repr=False, compare=False)

        def __call__(self, central_angle: float):
            from gpdk.components.bend.bend_circular import BendCircular
            radius_eff = self.radius_eff
            bend = BendCircular(degrees=math.degrees(central_angle), radius=radius_eff, waveguide_type=self.waveguide_type)
            return bend, radius_eff, ("op_0", "op_1")

    user_defined_bend_factory = user_defined_bendfactory(radius_eff=10, waveguide_type=TECH.WG.SWG.C.WIRE)

  Then users can decide to use the defined ``user_defined_bendfactory`` in the link function or they can simply enter ``TECH.WG.FWG.C.WIRE.BEND_CIRCULAR`` if they define ``BEND_CIRCULAR`` and ``BEND_EULER`` under ``TECH.WG.FWG.C.WIRE``. The choose of use depends entirely on the user's consideration of the performance of the device::

        link1 = fp.create_links(
            link_type=TECH.WG.FWG.C.EXPANDED,
            # bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR,
            bend_factory=user_defined_bend_factory,
            specs=[
                wg1["op_0"] >> wg2["op_1"],
                wg1["op_1"] >> wg3["op_1"],
            ],
        )





