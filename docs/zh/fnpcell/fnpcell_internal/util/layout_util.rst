Module fnpcell.internal.util.layout_util
=========================================

Functions
-------------

get_bounding_box
+++++++++++++++++++

::
    
    def get_bounding_box(target: IRunnable, *, exclude_layers: Iterable[ILayer] = ()) -> Tuple[Tuple[float, float], Tuple[float, float]]

Returns bounding box of target.

Attributes
_____________

target
    any drawable instance, such as IPolygon, ICell, ICellRef, ILibrary …

Returns
    (x_min,y_min,x_max,y_max) Usage::
        
        (x_min, y_min), (x_max, y_max) = fp.get_bounding_box(cell)