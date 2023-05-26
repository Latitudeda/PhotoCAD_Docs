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
    fp.el.EllipticalArc
    fp.el.EllipticalRing


* ``fp.el.Rect``
    * parameters: width/height/center/origin/bottom_left/transform/corner_radius/layer
    * examples:

        ::
            ``rect = fp.el.Rect(width=10, height=10, center=(0, 0), layer=TECH.LAYER.FWG_COR)``
            ``fp.el.Rect(width=8, height=8, center=(10, 0), layer=TECH.LAYER.M1_DRW, corner_radius=2)``

        .. image:: ../images/rect.png


* ``fp.el.Circle``
    test2
* ``fp.el.Polygon``
* ``fp.el.Rect``
* ``fp.el.Rect``
* ``fp.el.Rect``
* ``fp.el.Rect``



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

For specific usage, please refer to :doc:`../WaveguideRouting/Summary`.

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

