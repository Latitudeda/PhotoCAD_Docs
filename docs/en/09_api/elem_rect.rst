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
   :widths: 22 22 46
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``width``
     - Required
     - Rectangle width in layout units.
   * - ``height``
     - Required
     - Rectangle height in layout units.
   * - ``corner_radius``
     - ``0``
     - Radius of the rectangle corner. A single number rounds all corners.
       A sequence can be used to control different corners.
   * - ``bottom_left``
     - ``None``
     - Places the rectangle by its bottom-left coordinate.
   * - ``origin``
     - ``None``
     - Alternative placement coordinate supported by the factory function.
   * - ``center``
     - ``None``
     - Places the rectangle by its center coordinate.
   * - ``transform``
     - Identity transform
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - Required
     - Technology layer where the rectangle is drawn.

Basic Usage
-----------

The following examples create a normal rectangle and a rounded rectangle.

.. code-block:: python

    fp.el.Rect(
        width=10,
        height=10,
        center=(0, 0),
        layer=TECH.LAYER.FWG_COR,
    )

    fp.el.Rect(
        width=8,
        height=8,
        center=(10, 0),
        corner_radius=2,
        layer=TECH.LAYER.M1_DRW,
    )

.. image:: image/elem_rect_basic.png
   :align: center
   :width: 520px
