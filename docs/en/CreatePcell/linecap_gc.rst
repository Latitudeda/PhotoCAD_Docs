Grating Coupler with linecap
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This grating coupler design is used to avoid DRC error at places where turning angle < 90 degree.

Full script
--------------------------------------------------------

 ::

        import math
        from fnpcell import all as fp
        from typing_extensions import Tuple, List, cast
        from gpdk import all as pdk
        from gpdk.technology import get_technology
        from gpdk.technology.wg.types import CoreCladdingWaveguideType


        class GC_linecap(fp.PCell):

            length: float = fp.PositiveFloatParam(default=25.0)
            half_degrees: float = fp.DegreeParam(default=20)
            ellipse_ratio: float = fp.PositiveFloatParam(default=1.0, min=1.0, doc="Ellipse(Major/Minor)")
            tooth_width: float = fp.PositiveFloatParam(default=0.5)
            etch_width: float = fp.PositiveFloatParam(default=0.5)
            teeth: int = fp.IntParam(default=30, min=0, doc="Number of tooth")
            waveguide_type: CoreCladdingWaveguideType = fp.WaveguideTypeParam(type=CoreCladdingWaveguideType, default=fp.USE_DEFAULT_FACTORY)
            port_names: fp.IPortOptions = fp.PortOptionsParam(count=2, default=("op_0", "optfiber"))

            def _default_waveguide_type(self):
                return get_technology().WG.FWG.C.WIRE

            def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
                insts, elems, ports = super().build()
                TECH = get_technology()

                length = self.length
                half_degrees = self.half_degrees
                ellipse_ratio = self.ellipse_ratio
                tooth_width = self.tooth_width
                etch_width = self.etch_width
                teeth = self.teeth
                waveguide_type = self.waveguide_type
                port_names = self.port_names

                overlap = 1.0
                fiber_pin_width = 5

                half_angle = math.radians(half_degrees)
                waveguide_width = waveguide_type.core_width
                waveguide_cladding = waveguide_type.cladding_width
                waveguide_layer = waveguide_type.core_layer
                cladding_layer = waveguide_type.cladding_layer
                si_etch1_layer = TECH.WG.MWG.C.WIRE.core_layer
                fbrtgt = TECH.LAYER.FIBREC_NOTE


                content: List[fp.IPolygon] = [
                    fp.el.EllipticalRing(outer_radius=(length, length / ellipse_ratio), layer=waveguide_layer,
                                         initial_degrees=-half_degrees, final_degrees=half_degrees)]

                final_tooth_radius = length
                for _ in range(teeth):
                    final_tooth_radius = final_tooth_radius + etch_width + tooth_width

                    curve = fp.g.Arc(radius=final_tooth_radius - tooth_width / 2,
                                     initial_degrees=-half_degrees,
                                     final_degrees=half_degrees)
                    content.append(fp.el.Curve(curve, stroke_width=tooth_width, layer=TECH.LAYER.FWG_COR,
                                               line_cap=(fp.el.LineCapRound(), fp.el.LineCapRound())))

                triangle_h = (waveguide_width / 2.0) / math.tan(half_angle)
                triangle = fp.el.Polygon(raw_shape=[(0, 0), (triangle_h, waveguide_width / 2.0), (triangle_h, - waveguide_width / 2.0)], layer=waveguide_layer)

                content = list(fp.el.PolygonSet(content, layer=waveguide_layer) - triangle)

                fiber_pin_tooth = 1 + int(teeth / 2)  # 1 for wedge_polygon
                fiber_pin_x = min(content[fiber_pin_tooth].polygon_points, key=lambda p: p[0])[0]

                cladding_x = final_tooth_radius + waveguide_cladding / 2
                cladding_y = cladding_x / ellipse_ratio

                cladding_polygon = fp.el.EllipticalRing(outer_radius=(cladding_x, cladding_y), layer=cladding_layer, transform=fp.rotate(radians=math.pi))
                trapezoid = fp.el.Line(length=cladding_x - triangle_h,
                                       stroke_width=waveguide_cladding,
                                       final_stroke_width=math.tan(half_angle) * cladding_x * 2 + waveguide_cladding,
                                       layer=cladding_layer).translated(triangle_h, 0)
                cladding_polygon &= trapezoid
                content.append(trapezoid)


                rec_end = fp.el.Rect(width=2, height=math.tan(half_angle) * cladding_x * 2 + waveguide_cladding, layer=cladding_layer, center=(cladding_x + 1, 0))
                content.append(rec_end)

                # fiber port
                elements = cast(List[fp.IElement], content)
                elements.extend(
                    [
                        fp.el.Line(length=fiber_pin_width, stroke_width=fiber_pin_width, layer=fbrtgt, transform=fp.translate(fiber_pin_x, 0)),
                        fp.el.Text(content="optFiber", text_anchor=fp.Anchor.CENTER, vertical_align=fp.VertialAlign.MIDDLE, layer=fbrtgt, at=(fiber_pin_x + fiber_pin_width / 2, 0)),
                    ]
                )

                elems += elements


                s = pdk.Straight(length=5, waveguide_type=waveguide_type)
                s_left = fp.place(s, "op_1", at=(triangle_h, 0))
                insts += s_left

                ports += s_left["op_0"].with_name(port_names[0])
                ports += fp.Port(name=port_names[1], position=(fiber_pin_x + fiber_pin_width / 2, 0), orientation=0,
                                 shape=fp.g.Rect(width=fiber_pin_width, height=fiber_pin_width,
                                 center=(fiber_pin_x + fiber_pin_width / 2, 0)), waveguide_type=waveguide_type)

                return insts, elems, ports

Section Script Description
===========================

#. User-defined parameters:

    ::

        length: float = fp.PositiveFloatParam(default=25.0) # Length of the grating taper
        half_degrees: float = fp.DegreeParam(default=20) # Angle of the grating taper
        ellipse_ratio: float = fp.PositiveFloatParam(default=1.0, min=1.0, doc="Ellipse(Major/Minor)") # The aspect ratio of the ellipse
        tooth_width: float = fp.PositiveFloatParam(default=0.5) # Width of the grating
        etch_width: float = fp.PositiveFloatParam(default=0.5) # Spacing of the grating
        teeth: int = fp.IntParam(default=30, min=0, doc="Number of tooth") # Number of grating



#. Layout added in the build method:

   #. Create content list and generate grating sector:

       Define a list called content, filled with a circular sector generated with ``fp.el.EllipticalRing`` with radius ``length`` and angle ``[-half_degrees, half_degrees]``.

        ::

            content: List[fp.IPolygon] = [fp.el.EllipticalRing(outer_radius=(length, length / ellipse_ratio), layer=waveguide_layer,initial_degrees=-half_degrees, final_degrees=half_degrees)]

        .. image:: ../images/GC_1.png

   #. Generate grating tooth and capped line on the edge of the tooth

        Generate a curve with ``fp.g.Arc``, pass it into ``fp.el.Curve`` to draw a grating along the curve with a width of ``tooth_width`` and a rounded ***line_cap***. ***Line_cap*** can use rounded ``fp.el.LineCapRound()`` or triangular ``fp.el.LineCapTriangle(ratio=0.3)``, where ``ratio`` is the ratio of the height and base of the triangle, so that if ratio<0.5, then the top angle of the line_cap is >90°. (Generating the triangle linecap requires fewer points and runs faster.)

         ::

            final_tooth_radius = length
            for _ in range(teeth):
                final_tooth_radius = final_tooth_radius + etch_width + tooth_width

                curve = fp.g.Arc(radius=final_tooth_radius - tooth_width / 2,
                                 initial_degrees=-half_degrees,
                                 final_degrees=half_degrees)
                content.append(fp.el.Curve(curve, stroke_width=tooth_width, layer=TECH.LAYER.FWG_COR,
                                           line_cap=(fp.el.LineCapRound(), fp.el.LineCapRound())))


        .. image:: ../images/GC_2_round.png
        .. image:: ../images/GC_2_tri.png
        .. image:: ../images/GC_2.png


   #. Trim the input port to connect with waveguide

        Generate an equilateral triangle with height ``triangle_h`` and base ``waveguide_width`` using ``fp.el.Polygon``, do a boolean operation ``-`` on the triangle and the sector, and truncate the top corner of the left side of the sector for subsequent connection of a straight waveguide here.

         ::

            triangle_h = (waveguide_width / 2.0) / math.tan(half_angle)
            triangle = fp.el.Polygon(raw_shape=[(0, 0), (triangle_h, waveguide_width / 2.0), (triangle_h, - waveguide_width / 2.0)], layer=waveguide_layer)

            content = list(fp.el.PolygonSet(content, layer=waveguide_layer) - triangle)

        .. image:: ../images/GC_3.png


   #. Add cladding layer

        Add trapezoidal cladding.


        ::

            cladding_x = final_tooth_radius + waveguide_cladding / 2
            cladding_y = cladding_x / ellipse_ratio

            cladding_polygon = fp.el.EllipticalRing(outer_radius=(cladding_x, cladding_y), layer=cladding_layer, transform=fp.rotate(radians=math.pi))
            trapezoid = fp.el.Line(length=cladding_x - triangle_h,
                                   stroke_width=waveguide_cladding,
                                   final_stroke_width=math.tan(half_angle) * cladding_x * 2 + waveguide_cladding,
                                   layer=cladding_layer).translated(triangle_h, 0)
            cladding_polygon &= trapezoid
            content.append(trapezoid)

        .. image:: ../images/GC_4.png


   #. Add straight waveguide for connection and left rectangle to avoid DRC error

        Add rectangles on the right to avoid having <90° bends and straight waveguides on the left to connect to other devices.

        ::

            rec_end = fp.el.Rect(width=2, height=math.tan(half_angle) * cladding_x * 2 + waveguide_cladding, layer=cladding_layer, center=(cladding_x + 1, 0))
            content.append(rec_end)


            s = pdk.Straight(length=5, waveguide_type=waveguide_type)
            s_left = fp.place(s, "op_1", at=(triangle_h, 0))
            insts += s_left

        .. image:: ../images/GC_5.png



   #. Define the ports of the line capped grating coupler

        ::

            ports += s_left["op_0"].with_name(port_names[0])
            ports += fp.Port(name=port_names[1], position=(fiber_pin_x + fiber_pin_width / 2, 0), orientation=0,
                             shape=fp.g.Rect(width=fiber_pin_width, height=fiber_pin_width,
                             center=(fiber_pin_x + fiber_pin_width / 2, 0)), waveguide_type=waveguide_type)


Run the script and view the layout
=========================================
Run ``grating_coupler_linecap.py`` and use layout tool e.g. KLayout to view the generated GDS file, which should be saved under ``gpdk`` > ``components`` > ``grating_coupler`` > ``local``.

        .. image:: ../images/GC_6.png