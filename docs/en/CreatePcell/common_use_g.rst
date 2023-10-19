fp.g API
==================================

``fp.g`` API generates varies of curves which is often used with ``waveguide_type`` to define the path of a waveguide type. Cells create by ``fp.g.`` has no layer information hence cannot be as a element or an instance in the ``build`` function.

Here we list some examples where ``fp.g.`` is mostly often used.

#. ::

        euler_curve = fp.g.EulerBend() # define in raw_curve method
        wg = waveguide_type(curve=euler_curve) # define in build method
        insts += wg

``fp.g``
-----------------

The api for geometry mainly contains::

    fp.g.Arc
    fp.g.Bezier
    fp.g.Circle
    fp.g.CosineBend
    fp.g.EllipticalArc
    fp.g.EllipticalRing
    fp.g.EulerBend
    fp.g.FakeCurve
    fp.g.Line
    fp.g.Polyline
    fp.g.Rect
    fp.g.RegularPolygon
    fp.g.Ring
    fp.g.Shape

#. ``fp.g.Arc``
    * parameters
        * radius
        * initial_radians/degrees
        * final_radians/degrees
        * origin
        * transform

#. ``fp.g.Bezier``
    * parameters
        * start
        * controls
        * end
        * origin
        * transform

#. ``fp.g.Circle``
    * parameters
        * radius
        * initial_radians/degrees
        * final_radians/degrees
        * origin
        * transform

#. ``fp.g.CosineBend``
    * parameters
        * radius_min
        * radians/degrees
        * p
        * l_max
        * angle_step
        * origin
        * transform

#. ``fp.g.EllipticalArc``
    * parameters
        * radius
        * initial_radians/degrees
        * final_radians/degrees
        * origin
        * transform

#. ``fp.g.EllipticalRing``
    * parameters
        * outer_radius/inner_radius
        * initial_radians/degrees
        * initial_radians/initial_degrees
        * final_radians/final_degrees
        * origin
        * transform

#. ``fp.g.EulerBend``
    * parameters
        * radius_min
        * radians/degrees
        * p
        * l_max
        * angle_step
        * origin
        * transform

#. ``fp.g.FakeCurve``
    * parameters
        * start
        * end
        * curve_length
        * transform

#. ``fp.g.Line``
    * parameters
        * length
        * step
        * anchor
        * origin
        * transform

#. ``fp.g.Polyline``
    * parameters
        * raw_points
        * raw_end_orientations
        * transform

#. ``fp.g.Rect``
    * parameters
        * width
        * height
        * corner_radii
        * transform

#. ``fp.g.RegularPolygon``
    * parameters
        * sides
        * side_length
        * transform

#. ``fp.g.Ring``
    * parameters
        * outer_radius
        * inner_radius
        * initial_radians/degrees
        * final_radians/degrees
        * origin
        * transform

#. ``fp.g.Shape``
    * parameters
        * raw_shape_points
        * origin
        * transform










