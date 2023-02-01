工具类api
====================

工具类api主要包含::

    translated
    rotated
    h_mirror
    v_mirror
    repositioned
    position
    get_bounding_box

translated

repositioned

Positioned at new point,Owner will translated.

rotated

Rotated both degrees and radians.

Returns bounding box of target.

Attributes
target
any drawable instance, such as IPolygon, ICell, ICellRef, ILibrary …
Returns
(x_min,y_min,x_max,y_max) Usage:

(x_min, y_min), (x_max, y_max) = fp.get_bounding_box(cell)