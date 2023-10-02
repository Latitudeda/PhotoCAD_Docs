Commonly used interface
==============================================

The main types of interface functions commonly used by users are as follows:

1. Graphics_
2. Routing_
3. Transform_
4. Information_

Graphics
^^^^^^^^^^^^^^

The graphics api mainly contains the api for common graphics drawing and the api for Boolean operations.

The api for common graphics mainly contains::

    fp.el.Rect
    fp.el.Circle
    fp.el.Polygon
    fp.el.Ring
    fp.el.RegularPolygon
    fp.el.Line
    fp.el.Label



* ``fp.el.Rect``
    * parameters: width/height/center/origin/bottom_left/transform/corner_radius/layer
    * examples:

            * ``fp.el.Rect(width=10, height=10, center=(0, 0), layer=TECH.LAYER.FWG_COR)``

            * ``fp.el.Rect(width=8, height=8, center=(10, 0), layer=TECH.LAYER.M1_DRW, corner_radius=2)``

        .. image:: ../images/rect.png


* ``fp.el.Circle``
    * parameters: radius/origin/initial_degrees/final_degrees/initial_radians/final_radians/transform/layer
    * examples:

            * ``fp.el.Circle(radius=10, origin=(0, 0), initial_degrees=30, final_degrees=90, layer=TECH.LAYER.M1_DRW)``

            * ``fp.el.Circle(radius=8, origin=(15, 0), initial_degrees=0, final_degrees=120, layer=TECH.LAYER.N_DRW)``

        .. image:: ../images/circle.png

* ``fp.el.Polygon``
    * parameters: raw_shape/origin/transform/layer
    * examples:

            * ``fp.el.Polygon(raw_shape=[(0, 0), (6, 2), (7, 8), (2, 12)], origin=(0, 0), layer=TECH.LAYER.M2_DRW)``

            * ``fp.el.Polygon(raw_shape=[(3, 5), (6, 9), (11, 15), (4, 12)], origin=(10, 0), layer=TECH.LAYER.GE_DRW)``

        .. image:: ../images/polygon.png

* ``fp.el.ring``
    * parameters: outer_radius/inner_radius/origin/initial_degrees/final_degrees/initial_radians/final_radians/transform/layer
    * examples:

            * ``fp.el.Ring(outer_radius=5, inner_radius=2, initial_degrees=30, final_degrees=120, layer=TECH.LAYER.TIN_DRW)``

            * ``fp.el.Ring(outer_radius=8, inner_radius=3, initial_degrees=0, final_degrees=90, origin=(10, 0), layer=TECH.LAYER.PINREC_TEXT)``

        .. image:: ../images/ring.png

* ``fp.el.RegularPolygon``
    * parameters: sides/side_length/origin/transform/layer
    * examples:

            * ``fp.el.RegularPolygon(sides=3, side_length=5, layer=TECH.LAYER.IOPORT_EREC)``

            * ``fp.el.RegularPolygon(sides=5, side_length=7, origin=(10, 0), layer=TECH.LAYER.PASS_MT)``

        .. image:: ../images/regularpolygon.png

* ``fp.el.Line``
    * parameters: length/stroke_width/final_stroke_width/stroke_offset/final_stroke_offset/taper_function/end_hints/anchor/origin/transform/layer
    * examples:

            * ``fp.el.Line(length=10, stroke_width=5, final_stroke_width=8, layer=TECH.LAYER.NP_DRW)``

            * ``fp.el.Line(length=10, stroke_width=3, final_stroke_width=5, stroke_offset=2, final_stroke_offset=5, anchor=fp.Anchor.CENTER, origin=(0, 5), layer=TECH.LAYER.PP_DRW)``

        .. image:: ../images/line.png

* ``fp.el.Label``
    * parameters: content/highlight/baseline/at/font/font_size/origin/anchor/transform/layer
    * examples:

            * ``from gpdk.technology.font.font_std_vented import FONT as font``

            * ``label = fp.el.Label(content="LDA", highlight=True, at=(0, 0), font=font, font_size=10, layer=TECH.LAYER.LABEL_DRW)``

            * ``fp.el.Label(content="PHOTOCAD", highlight=False, at=(0, 12), font=font, font_size=15, layer=TECH.LAYER.TEXT_NOTE)``

        .. image:: ../images/label.png


To change the layer of an element from one component to another, users are allow to use ``fp.el.PolygonSet.with_layer()``  to easily adjust the layer of the element  from one to another::

    fp.el.PolygonSet.with_layer(self="polygon you wish to tranform", layer="the layer you wish the transformed polygon to be")

The Boolean api mainly contains::

    bool = rect | circ
    bool = rect & circ
    bool = rect - circ
    bool = rect ^ circ


Routing
^^^^^^^^^^^^^^^
The routing api mainly contains::

    fp.Linked
    fp.LinkBetween
    fp.create_links
    fp.Connect

For specific usage, please refer to :doc:`../Circuit_design/waveguide_routing`.

Transform
^^^^^^^^^^^^^^
The transform api mainly contains::

    translated
    rotated
    h_mirrored
    v_mirrored
    c_mirrored
    scaled
    repositioned


Information
^^^^^^^^^^^^^^
The information api mainly contains::

    position:
     # return port's position (x, y)
    orientation:
     # return port's orientation (radian)
    get_left_ports:
     # return all left-sided ports in the PCell
    get_right_ports:
     # return all right-sided ports in the PCell
    get_bounding_box(target, exclude_layers):
     # return the bounding box's coordinate of the PCell
     # target: any drawable instance, such as IPolygon, ICell, ICellRef, ILibrary
     # exclude_layers: layers you don't want the function to be included.

