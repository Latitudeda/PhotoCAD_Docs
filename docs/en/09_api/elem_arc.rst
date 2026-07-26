.. _api_elem_arc:

Arc
===

``fp.el.Arc`` creates a stroked circular arc on a specified technology layer.
It can use a constant width or taper between different widths and offsets along
the arc.

The function definition is available in
``fnpcell`` > ``element`` > ``arc.pyi``.

Parameters
----------

.. list-table::
   :widths: 18 24 27 41
   :header-rows: 1

   * - Parameter
     - Type
     - Example
     - Description
   * - ``radius``
     - ``float``
     - ``8``
     - Radius of the circular centerline in layout units.
   * - ``stroke_width``
     - ``float``
     - ``2``
     - Width at the start of the arc.
   * - ``final_stroke_width``
     - ``Optional[float]``
     - ``4``
     - Width at the end of the arc.
   * - ``stroke_offset``
     - ``float``
     - ``0.5``
     - Offset from the circular centerline at the start of the arc.
   * - ``final_stroke_offset``
     - ``Optional[float]``
     - ``1.5``
     - Offset from the circular centerline at the end of the arc.
   * - ``taper_function``
     - ``ITaperCallable``
     - ``fp.TaperFunction.LINEAR``
     - Controls how the width and offset change from start to end.
   * - ``initial_radians``
     - ``Optional[float]``
     - ``0``
     - Initial angle in radians.
   * - ``initial_degrees``
     - ``Optional[float]``
     - ``0``
     - Initial angle in degrees.
   * - ``final_radians``
     - ``Optional[float]``
     - ``1.5708``
     - Final angle in radians.
   * - ``final_degrees``
     - ``Optional[float]``
     - ``120``
     - Final angle in degrees.
   * - ``angle_step``
     - ``Optional[float]``
     - ``0.05``
     - Angular sampling step in radians.
   * - ``extension``
     - ``Tuple[float, float]``
     - ``(1, 2)``
     - Straight extension lengths at the start and end of the arc.
   * - ``line_cap``
     - ``Tuple[Optional[ILineCap], Optional[ILineCap]]``
     - ``(fp.el.LineCapRound(), fp.el.LineCapRound())``
     - Optional cap shapes at the start and end of the arc.
   * - ``origin``
     - ``Optional[Point2D]``
     - ``(0, 0)``
     - Center coordinate of the arc.
   * - ``transform``
     - ``Affine2D``
     - ``fp.translate(0, 2)``
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - ``ILayer``
     - ``TECH.LAYER.M1_DRW``
     - Technology layer where the arc is drawn.

When no initial or final angle is specified, the element follows a full
``360``-degree circular path. Angular limits can be supplied in either radians
or degrees.

Basic Usage
-----------

The following examples cover every parameter listed above. The first arc uses
degree angles, tapered width and offset, end extensions, line caps, and a
transform. The second arc demonstrates the alternative radian angle inputs.

.. code-block:: python

    arc_degrees = fp.el.Arc(
        radius=8,
        stroke_width=2,
        final_stroke_width=4,
        stroke_offset=0.5,
        final_stroke_offset=1.5,
        taper_function=fp.TaperFunction.LINEAR,
        initial_degrees=0,
        final_degrees=120,
        angle_step=0.05,
        extension=(1, 2),
        line_cap=(fp.el.LineCapRound(), fp.el.LineCapRound()),
        origin=(0, 0),
        transform=fp.translate(0, 2),
        layer=TECH.LAYER.M1_DRW,
    )

    arc_radians = fp.el.Arc(
        radius=6,
        stroke_width=1.5,
        initial_radians=0,
        final_radians=1.5708,
        origin=(24, 0),
        layer=TECH.LAYER.N_DRW,
    )

.. image:: image/elem_arc_basic.png
   :align: center
   :width: 520px
