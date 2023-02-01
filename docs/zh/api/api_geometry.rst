图形类api
====================

图形类api主要包含常用图形绘制的api以及布尔运算的api。

常用图形的api主要包含::

    fp.el.Rect
    fp.el.Circle
    fp.el.Polygon
    fp.el.Ring
    fp.el.RegularPolygon
    fp.el.Line
    fp.el.EllipticalArc
    fp.el.EllipticalRing

布尔运算api主要包含::

    bool = rect | circ
    bool = rect & circ
    bool = rect - circ
    bool = rect ^ circ

具体用法参照（:doc:`../Tutorials/Step1`）