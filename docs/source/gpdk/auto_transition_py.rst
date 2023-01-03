auto_transition_py
============================================================

该脚本主要定义了端口连接时的波导类型与默认弯曲波导::

脚本为::

    from typing import Tuple, cast
    from fnpcell.pdk.technology import all as fpt
    from .interfaces import CoreCladdingWaveguideType
    from .wg import WG

    def _c_fwg2mwg(end_types: Tuple[fpt.IWaveguideType, fpt.IWaveguideType]):
        from ..components.transition.fwg2mwg_transition import FWG2MWGTransition

        a = end_types[0]
        b = end_types[1]
        assert isinstance(a, WG.FWG.C)
        assert isinstance(b, WG.MWG.C)

        return FWG2MWGTransition(name="auto", length=20, fwg_type=a, mwg_type=b), ("op_0", "op_1")


    def _c_fwg2swg(end_types: Tuple[fpt.IWaveguideType, fpt.IWaveguideType]):
        from ..components.transition.fwg2swg_transition import FWG2SWGTransition

        a = end_types[0]
        b = end_types[1]
        assert isinstance(a, WG.FWG.C)
        assert isinstance(b, WG.SWG.C)

        return FWG2SWGTransition(name="auto", length=20, fwg_type=a, swg_type=b), ("op_0", "op_1")


    def _c_swg2mwg(end_types: Tuple[fpt.IWaveguideType, fpt.IWaveguideType]):
        from ..components.transition.swg2mwg_transition import SWG2MWGTransition

        a = end_types[0]
        b = end_types[1]
        assert isinstance(a, WG.SWG.C)
        assert isinstance(b, WG.MWG.C)

        return SWG2MWGTransition(name="auto", swg_length=10, mwg_length=10, swg_type=a, mwg_type=b), ("op_0", "op_1")


    class _Taper:
        def __init__(self, slope: float) -> None:
            self.slope = slope

        def __call__(self, end_types: Tuple[fpt.IWaveguideType, fpt.IWaveguideType]):
            from ..components.taper.taper_linear import TaperLinear

            a = cast(CoreCladdingWaveguideType, end_types[0])
            b = cast(CoreCladdingWaveguideType, end_types[1])
            k = self.slope
            length = max(0.01, abs(a.core_width - b.core_width) / k)
            return TaperLinear(name="auto", length=length, left_type=a, right_type=b), ("op_0", "op_1")


    class AUTO_TRANSITION:
        @fpt.classconst
        @classmethod
        def DEFAULT(cls):
            return fpt.AutoTransition().updated(
                [
                    (WG.FWG.C >> WG.MWG.C, _c_fwg2mwg),
                    (WG.FWG.C >> WG.SWG.C, _c_fwg2swg),
                    (WG.SWG.C >> WG.MWG.C, _c_swg2mwg),
                    #
                    (WG.FWG.C >> WG.FWG.C, _Taper(0.2)),
                    (WG.SWG.C >> WG.SWG.C, _Taper(0.2)),
                    (WG.MWG.C >> WG.MWG.C, _Taper(0.2)),
                ]
            )