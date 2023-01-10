Step 1: Build basic building blocks 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This case implements the construction of three basic building blocks, including:

- Bend_
- Straight_waveguide_
- Taper_

Bend
---------------------------------------
Define bend::

    class BendCircular(fp.IWaveguideLike, fp.PCell):
        degrees: float = fp.DegreeParam(default=90, min=-180, max=180, doc="Bend angle in degrees")
        radius: float = fp.PositiveFloatParam(default=10, doc="Bend radius")
        waveguide_type: fp.IWaveguideType = fp.WaveguideTypeParam(doc="Waveguide parameters")
        port_names: fp.IPortOptions = fp.PortOptionsParam(count=2, default=["op_0", "op_1"])

        def _default_waveguide_type(self):
            return get_technology().WG.FWG.C.WIRE

        def __post_pcell_init__(self):
            assert fp.is_nonzero(self.degrees)

        @cached_property
        def raw_curve(self):
            return fp.g.EllipticalArc(
                radius=self.radius,
                final_degrees=self.degrees,
            )

        def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
            insts, elems, ports = super().build()
            wg = self.waveguide_type(curve=self.raw_curve).with_ports(self.port_names)
            insts += wg
            ports += wg.ports
            return insts, elems, ports
    
call class, generate the bend waveguide layout file and plot::
    
        library += BendCircular(name="s", radius=15, waveguide_type=TECH.WG.FWG.C.WIRE)
        fp.export_gds(library, file=gds_file)
        fp.plot(library)
        
Bend waveguide


Straight Waveguide
-----------------------------------
Define Straight waveguide::

    class Straight(fp.IWaveguideLike, fp.PCell):
        length: float = fp.FloatParam(default=10, min=0)
        waveguide_type: fp.IWaveguideType = fp.WaveguideTypeParam()
        anchor: fp.Anchor = fp.AnchorParam(default=fp.Anchor.START)
        port_names: fp.IPortOptions = fp.PortOptionsParam(count=2, default=("op_0", "op_1"))

        def _default_waveguide_type(self):
            return get_technology().WG.FWG.C.WIRE

        @cached_property
        def raw_curve(self):
            return fp.g.Line(
                length=self.length,
                anchor=self.anchor,
            )

        def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
            insts, elems, ports = super().build()
            wg = self.waveguide_type(curve=self.raw_curve).with_ports(self.port_names)
            insts += wg
            ports += wg.ports
            return insts, elems, ports

call class, generate the staright waveguide layout file and plot::

        library += Straight(name="s", length=10, waveguide_type=TECH.WG.FWG.C.WIRE)
        fp.export_gds(library, file=gds_file)
        fp.plot(library)

Straight waveguide

Taper
--------------------------------------
Define Taper waveguide::

     class TaperLinear(fp.IWaveguideLike, fp.PCell):
        length: float = fp.PositiveFloatParam(default=10)
        left_type: CoreCladdingWaveguideType = fp.WaveguideTypeParam(type=CoreCladdingWaveguideType)
        right_type: CoreCladdingWaveguideType = fp.WaveguideTypeParam(type=CoreCladdingWaveguideType)
        anchor: fp.Anchor = fp.AnchorParam(default=fp.Anchor.CENTER)
        port_names: fp.IPortOptions = fp.PortOptionsParam(count=2, default=["op_0", "op_1"])

        def _default_left_type(self):
            return get_technology().WG.FWG.C.WIRE

        def _default_right_type(self):
            return get_technology().WG.FWG.C.EXPANDED

        @cached_property
        def raw_curve(self):
            return fp.g.Line(
                length=self.length,
                anchor=self.anchor,
            )

        def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
            insts, elems, ports = super().build()
            assert self.left_type.is_isomorphic_to(self.right_type), "left_type must be isomorphic to right_type"

            wgt = self.left_type.tapered(taper_function=fp.TaperFunction.LINEAR, final_type=self.right_type)
            wg = wgt(curve=self.raw_curve).with_ports(self.port_names)
            insts += wg
            ports += wg.ports
            return insts, elems, ports


call class, generate the taper waveguide layout file and plot::

    library += TaperLinear(length=20, left_type=TECH.WG.SWG.C.WIRE, right_type=TECH.WG.SWG.C.EXPANDED)
    fp.export_gds(library, file=gds_file)
    fp.plot(library)
    
Taper waveguide


