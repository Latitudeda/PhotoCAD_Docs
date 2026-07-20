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
   :widths: 22 22 46
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``radius``
     - Required
     - Radius of the circular centerline in layout units.
   * - ``stroke_width``
     - ``1``
     - Width at the start of the arc.
   * - ``final_stroke_width``
     - ``None``
     - Width at the end of the arc. It uses ``stroke_width`` when omitted.
   * - ``stroke_offset``
     - ``0``
     - Offset from the circular centerline at the start of the arc.
   * - ``final_stroke_offset``
     - ``None``
     - Offset at the end of the arc. It uses ``stroke_offset`` when omitted.
   * - ``taper_function``
     - ``TaperLinear()``
     - Controls how the width and offset change from start to end.
   * - ``initial_radians``
     - ``None``
     - Initial angle in radians.
   * - ``initial_degrees``
     - ``None``
     - Initial angle in degrees.
   * - ``final_radians``
     - ``None``
     - Final angle in radians.
   * - ``final_degrees``
     - ``None``
     - Final angle in degrees.
   * - ``angle_step``
     - ``None``
     - Angular sampling step in radians. An automatic value is used when omitted.
   * - ``extension``
     - ``(0, 0)``
     - Straight extension lengths at the start and end of the arc.
   * - ``line_cap``
     - ``(None, None)``
     - Optional cap shapes at the start and end of the arc.
   * - ``origin``
     - ``None``
     - Center coordinate of the arc.
   * - ``transform``
     - Identity transform
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - Required
     - Technology layer where the arc is drawn.

When no initial or final angle is specified, the element follows a full
``360``-degree circular path. Angular limits can be supplied in either radians
or degrees.

Basic Usage
-----------

The following examples create a constant-width arc and a tapered arc. The
second arc is translated upward after creation so that both results can be
viewed separately.

.. code-block:: python

    fp.el.Arc(
        radius=5,
        initial_degrees=0,
        final_degrees=90,
        stroke_width=5,
        layer=TECH.LAYER.M1_DRW,
    )

    fp.el.Arc(
        radius=5,
        initial_degrees=30,
        final_degrees=120,
        stroke_width=3,
        final_stroke_width=5,
        layer=TECH.LAYER.M1_DRW,
    ).translated(0, 10)

.. image:: image/elem_arc_basic.png
   :align: center
   :width: 520px
