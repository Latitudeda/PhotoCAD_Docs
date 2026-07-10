.. _api_elem_rect:

Rect
====

``fp.el.Rect`` creates a rectangular layout element on a specified technology
layer. It is one of the most common ``fp.el`` graphics APIs. In GPDK components,
rectangles are often used for bond pads, metal boxes, contact openings, heater
regions, marker shapes, and other simple layout blocks.

The public call is:

.. code-block:: python

    fp.el.Rect(
        width=10,
        height=5,
        center=(0, 0),
        layer=TECH.LAYER.M1_DRW,
    )

The function definition can be checked in
``fnpcell`` > ``element`` > ``rect.pyi``. Through ``fnpcell.all``, the
lower-level ``rect`` factory is exposed as ``fp.el.Rect``.

Basic Usage
-----------

The simplest usage is to provide the rectangle size, position, and layer.

.. code-block:: python

    import fnpcell.all as fp
    from gpdk.technology import get_technology

    TECH = get_technology()

    rect = fp.el.Rect(
        width=10,
        height=10,
        center=(0, 0),
        layer=TECH.LAYER.FWG_COR,
    )

    fp.plot(rect)

This creates a ``10 um x 10 um`` rectangle centered at the origin. The
``layer`` parameter decides which GDS layer the rectangle is drawn on.

.. image:: image/elem_rect_basic.png
   :align: center
   :width: 520px

Full Script
-----------

The following script creates two rectangles: one normal rectangle and one
rounded rectangle. It also shows the common local workflow: preview the layout
with ``fp.plot`` and export the same content to a GDS file with
``fp.export_gds``.

.. code-block:: python

    import fnpcell.all as fp
    from gpdk.technology import get_technology

    TECH = get_technology()

    # A normal rectangle on the waveguide core layer.
    rect_core = fp.el.Rect(
        width=10,
        height=10,
        center=(0, 0),
        layer=TECH.LAYER.FWG_COR,
    )

    # A rounded rectangle on the metal layer.
    rect_metal = fp.el.Rect(
        width=8,
        height=8,
        center=(10, 0),
        corner_radius=2,
        layer=TECH.LAYER.M1_DRW,
    )

    library = fp.Library()
    library += rect_core
    library += rect_metal

    # Preview the layout locally.
    fp.plot(library)

    # Export the same layout to a GDS file.
    fp.export_gds(
        library,
        file=TECH.OUTPUT.local_output_file(__file__).with_suffix(".gds"),
    )

Section Script Description
--------------------------

**Parameters:**

The main parameters are defined by ``fnpcell/element/rect.pyi``.

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
       Existing examples may still use this name.
   * - ``center``
     - ``None``
     - Places the rectangle by its center coordinate. This is the most common
       style in current GPDK examples.
   * - ``transform``
     - Identity transform
     - Applies a geometric transform when the element is created.
   * - ``layer``
     - Required
     - Technology layer where the rectangle is drawn.

**Create a normal rectangle:**

.. code-block:: python

    rect_core = fp.el.Rect(
        width=10,
        height=10,
        center=(0, 0),
        layer=TECH.LAYER.FWG_COR,
    )

``width`` and ``height`` define the rectangle size. ``center=(0, 0)`` puts the
center of the rectangle at the origin. ``TECH.LAYER.FWG_COR`` tells PhotoCAD
which process layer is used for this shape.

**Create a rounded rectangle:**

.. code-block:: python

    rect_metal = fp.el.Rect(
        width=8,
        height=8,
        center=(10, 0),
        corner_radius=2,
        layer=TECH.LAYER.M1_DRW,
    )

``corner_radius`` changes the rectangle corner from sharp to rounded. This is
useful when a layout needs a rectangular region with softened corners.

**Placement:**

``fp.el.Rect`` can be placed by ``center`` or ``bottom_left``. In many GPDK
components, ``center`` is used because it makes symmetric structures easier to
write.

.. code-block:: python

    centered_rect = fp.el.Rect(
        width=10,
        height=5,
        center=(0, 0),
        layer=TECH.LAYER.M1_DRW,
    )

    bottom_left_rect = fp.el.Rect(
        width=10,
        height=5,
        bottom_left=(0, 0),
        layer=TECH.LAYER.M1_DRW,
    )

If neither ``center`` nor ``bottom_left`` is provided, the position can become
ambiguous, so it is better to write one of them explicitly.

**Transform:**

Elements can be transformed after creation. This style is common when one base
shape is reused several times.

.. code-block:: python

    m1_box = fp.el.Rect(
        width=10,
        height=10,
        center=(0, 0),
        layer=TECH.LAYER.M1_DRW,
    )

    left_box = m1_box.translated(-10, 0)
    right_box = m1_box.translated(10, 0)

This pattern appears in GPDK components such as heater structures, where the
same metal box is placed on both sides of a central waveguide.

**Examples in GPDK:**

The same API is used in several GPDK component files.

.. code-block:: python

    # gpdk/components/bondpad/bondpad.py
    pad = fp.el.Rect(
        width=self.pad_width,
        height=self.pad_height,
        center=(0, 0),
        layer=TECH.LAYER.MT_DRW,
    )

.. code-block:: python

    # gpdk/components/heater/tin_heater.py
    m1_box = fp.el.Rect(
        width=metal_box_size,
        height=metal_box_size,
        center=(0, 0),
        layer=TECH.LAYER.M1_DRW,
    )

These examples show that ``fp.el.Rect`` is not only a demo API. It is used to
build real layout regions inside reusable components.

Run and view the layout
-----------------------

Save the full script in a Python file inside a PhotoCAD or GPDK project, then
run it with the project interpreter.

After running the script:

* ``fp.plot(library)`` opens a preview window.
* ``fp.export_gds(...)`` writes a GDS file to the local output path configured
  by ``TECH.OUTPUT.local_output_file(__file__)``.

If this page is edited in the documentation project, rebuild the local HTML
with:

.. code-block:: bat

    D:
    cd \photocad\PhotoCAD_Docs
    .\.venv\Scripts\activate.bat
    make_en

The generated page can then be viewed at:

.. code-block:: text

    build/html/09_api/elem_rect.html
