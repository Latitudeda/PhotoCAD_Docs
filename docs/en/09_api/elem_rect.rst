.. _api_elem_rect:

Rect
====

``fp.el.Rect`` creates a rectangular layout element on a specified technology
layer.

The function definition is available in
``fnpcell`` > ``element`` > ``rect.pyi``.

Parameters
----------

.. list-table::
   :widths: 18 24 27 41
   :header-rows: 1

   * - Parameter
     - Type
     - Example
     - Description
   * - ``width``
     - ``float``
     - ``10``
     - Rectangle width in layout units.
   * - ``height``
     - ``float``
     - ``8``
     - Rectangle height in layout units.
   * - ``corner_radius``
     - ``Union[float, Sequence[float]]``
     - ``(0, 1, 2, 3)``
     - Radius of the rectangle corner. A single number rounds all corners.
       A sequence can be used to control different corners.
   * - ``bottom_left``
     - ``Optional[Point2D]``
     - ``(8, -3)``
     - Places the rectangle by its bottom-left coordinate.
   * - ``origin``
     - ``Optional[Point2D]``
     - ``(20, 0)``
     - Legacy placement coordinate supported by the factory function.
       New code should use ``center`` or ``bottom_left``.
   * - ``center``
     - ``Optional[Point2D]``
     - ``(0, 0)``
     - Places the rectangle by its center coordinate.
   * - ``transform``
     - ``Affine2D``
     - ``fp.translate(0, 1)``
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - ``ILayer``
     - ``TECH.LAYER.FWG_COR``
     - Technology layer where the rectangle is drawn.

Basic Usage
-----------

The following examples cover every parameter listed above. They demonstrate
center placement, bottom-left placement, and the legacy ``origin`` placement
accepted by the factory function.

.. code-block:: python

    rect_center = fp.el.Rect(
        width=10,
        height=8,
        corner_radius=2,
        center=(0, 0),
        transform=fp.translate(0, 1),
        layer=TECH.LAYER.FWG_COR,
    )

    rect_bottom_left = fp.el.Rect(
        width=8,
        height=6,
        corner_radius=(0, 1, 2, 3),
        bottom_left=(8, -3),
        layer=TECH.LAYER.M1_DRW,
    )

    rect_origin = fp.el.Rect(
        width=6,
        height=4,
        origin=(20, 0),
        layer=TECH.LAYER.N_DRW,
    )

.. image:: image/elem_rect_basic.png
   :align: center
   :width: 520px
