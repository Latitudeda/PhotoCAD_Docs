.. _api_elem_circle:

Circle
======

``fp.el.Circle`` creates a circular layout element or a circular sector on a
specified technology layer.

The function definition is available in
``fnpcell`` > ``element`` > ``circle.pyi``.

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
     - Radius of the circle in layout units.
   * - ``initial_radians``
     - ``Optional[float]``
     - ``0``
     - Initial angle of the circular sector in radians.
   * - ``initial_degrees``
     - ``Optional[float]``
     - ``20``
     - Initial angle of the circular sector in degrees.
   * - ``final_radians``
     - ``Optional[float]``
     - ``2.4``
     - Final angle of the circular sector in radians.
   * - ``final_degrees``
     - ``Optional[float]``
     - ``160``
     - Final angle of the circular sector in degrees.
   * - ``origin``
     - ``Optional[Point2D]``
     - ``(0, 0)``
     - Center coordinate of the circle.
   * - ``transform``
     - ``Affine2D``
     - ``fp.translate(0, 1)``
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - ``ILayer``
     - ``TECH.LAYER.M1_DRW``
     - Technology layer where the circle is drawn.

When no initial or final angle is specified, the element is a full circle.
The angular limits can be supplied in either radians or degrees.

Basic Usage
-----------

The following examples cover every parameter listed above. The first sector
uses degree angles, while the second sector uses radian angles.

.. code-block:: python

    circle_degrees = fp.el.Circle(
        radius=8,
        origin=(0, 0),
        initial_degrees=20,
        final_degrees=160,
        transform=fp.translate(0, 1),
        layer=TECH.LAYER.M1_DRW,
    )

    circle_radians = fp.el.Circle(
        radius=6,
        origin=(18, 0),
        initial_radians=0,
        final_radians=2.4,
        transform=fp.translate(0, -1),
        layer=TECH.LAYER.N_DRW,
    )

.. image:: image/elem_circle_basic.png
   :align: center
   :width: 520px
