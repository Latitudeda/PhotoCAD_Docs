mmi
====================

多模干涉仪是光子继承链路的主要组件之一。

创建步骤如下:

导入库::

    from dataclasses import dataclass
    from typing import Tuple
    from fnpcell import all as fp
    from gpdk.components.straight.straight import Straight
    from gpdk.components.taper.taper_linear import TaperLinear
    from gpdk.technology import get_technology, PCell
    from gpdk.technology.interfaces import CoreCladdingWaveguideType

定义mmi类::

    @dataclass(eq=False)
    class Mmi(PCell):
        """
        Attributes:
            mid_wav_core_width: defaults to 5
            wav_core_width: defaults to 1
            n_inputs: defaults to 1
            n_outputs: defaults to 2
            length: defaults to 25
            transition_length: defaults to 5
            trace_spacing: defaults to 2
            waveguide_type: type of waveguide

        Examples:
        ```python
        TECH = get_technology()
            mmi = Mmi(waveguide_type=TECH.WG.FWG.C.WIRE)
        fp.plot(mmi)
        ```
        ![Mmi](images/mmi.png)
        """

        mid_wav_core_width: float = fp.PositiveFloatParam(default=5)
        wav_core_width: float = fp.PositiveFloatParam(default=1)
        # end_core_width=fp.PositiveFloatParam(default=0.45)
        n_inputs: int = fp.PositiveIntParam(default=1)
        n_outputs: int = fp.PositiveIntParam(default=2)
        length: float = fp.PositiveFloatParam(default=25)
        transition_length: float = fp.PositiveFloatParam(default=5)
        trace_spacing: float = fp.PositiveFloatParam(default=2)
        waveguide_type: CoreCladdingWaveguideType = fp.WaveguideTypeParam(type=CoreCladdingWaveguideType)

        def _default_waveguide_type(self):
            return get_technology().WG.FWG.C.WIRE

        def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
            insts, elems, ports = super().build()
            # fmt: off
            mid_wav_core_width = self.mid_wav_core_width
            wav_core_width=self.wav_core_width
            n_inputs = self.n_inputs
            n_outputs = self.n_outputs
            length = self.length
            transition_length = self.transition_length
            trace_spacing = self.trace_spacing
            waveguide_type = self.waveguide_type

            center_force_cladding_width = mid_wav_core_width+waveguide_type.cladding_width
            center_type = waveguide_type.updated(core_layout_width=mid_wav_core_width, cladding_layout_width=center_force_cladding_width)
            center = Straight(length=length, waveguide_type=center_type, anchor=fp.Anchor.START)
            insts += center

            wide_type = waveguide_type.updated(core_layout_width=wav_core_width, cladding_layout_width=waveguide_type.cladding_width + wav_core_width)
            narrow_type = waveguide_type#.updated(core_layout_width=end_core_width, cladding_layout_width=waveguide_type.cladding_width + end_core_width)
            taper_left = TaperLinear(length=transition_length, left_type=narrow_type, right_type=wide_type, anchor=fp.Anchor.END)
            taper_right = TaperLinear(length=transition_length, left_type=wide_type, right_type=narrow_type, anchor=fp.Anchor.START)

            base_in_y = - (n_inputs - 1) * trace_spacing / 2.0
            for cnt in range(n_inputs):
                taper_left_inst = taper_left.translated(0, base_in_y + cnt * trace_spacing)
                insts += taper_left_inst
                ports += taper_left_inst["op_0"].with_name(f"op_{n_inputs-cnt-1}")

            base_out_y = - (n_outputs - 1) * trace_spacing / 2.0
            for cnt in range(n_outputs):
                taper_right_inst = taper_right.translated(length, base_out_y + cnt * trace_spacing)
                insts += taper_right_inst
                ports += taper_right_inst["op_1"].with_name(f"op_{cnt + n_inputs}")

            # fmt: on
            return insts, elems, ports

定义一个1*2的mmi类::

    @dataclass(eq=False)
    class Mmi1x2(Mmi, locked=True):
        n_inputs: int = fp.PositiveIntParam(default=1)
        n_outputs: int = fp.PositiveIntParam(default=2)

这个类定义通过以下方法调用实现版图设计::

    library += Mmi1x2()
    fp.export_gds(library, file=gds_file)

运行案例，得到的版图文件为:

.. image:: ../images/comp_mmi.png