Commonly used interface
==============================================

The three main types of interface functions commonly used by users are as follows:

1. Graphics_
2. Routing_
3. Transform_

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
    fp.el.EllipticalArc
    fp.el.EllipticalRing

To change the layer of an element from one component to another, users are allow to use "fp.el.PolygonSet.with_layer()" to easily adjust the layer of the element  from one to another::

    fp.el.PolygonSet.with_layer(self="polygon you wish to tranform", layer="the layer you wish the transformed polygon to be")

The Boolean api mainly contains::

    bool = rect | circ
    bool = rect & circ
    bool = rect - circ
    bool = rect ^ circ

For specific usage, please refer to（:doc:`../Tutorials/Step1`）

Routing
^^^^^^^^^^^^^^^
The routing api mainly contains::

    fp.Linked
    fp.LinkBetween
    fp.creat_links
    fp.Connect

For specific usage, please refer to（:doc:`../WaveguideRouting/Summary`）

Transform
^^^^^^^^^^^^^^
The transform api mainly contains::

    translated
    rotated
    h_mirrored
    v_mirrored
    repositioned
    position
    get_bounding_box

