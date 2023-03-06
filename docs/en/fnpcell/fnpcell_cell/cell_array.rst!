Module fnpcell.cell.cell_array
===============================

Classes
--------

CellArray
++++++++++++

::

    class CellArray(cell: ICell, cols: int, col_end: Tuple[float, float], 
                    rows: int, row_end: Tuple[float, float], transform: Affine2D = Affine2D.identity())

CellArray is for defining a n*m Cell Array.

Any modification will create new CellArray instead of modify the original CellArray.

Ancestors
__________

::
    
    TransformMixin, IUpdatable, ICellArray, IElement, IRunnable, IAffineTransformable

Class variables
__________________

::

    var cell: ICell
    var col_end: Tuple[float, float]
    var cols: int
    var row_end: Tuple[float, float]
    var rows: int
    var transform: Affine2D

Static methods
________________

::

    def orthogonal(*, cell: ICell, cols: int, col_width: float, rows: int, row_height: float, 
                    transform: Affine2D = Affine2D.identity())
    
Return a cols*rows cell array.

::

    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None,
                             transform: Affine2D = Affine2D.identity()) -> Affine2D
    
**Inherited from:**  TransformMixin.transform_from_at   

Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, the …

::

    def transform_from_origin(origin: Optional[Tuple[float, float]] = None,
                                 transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_origin
            
Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, It …

Methods
________

::

    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::

    def decompose(self) -> Tuple[ICellRef, ...]

::

    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored
        
Horizontal mirrored.

::

    def polygon_set(self, *, layer: ILayer, union: bool = True) -> IPolygonSet

::

    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None,
                 origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** TransformMixin.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::

    def run(self, processor: IProcessor)

::

    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.scaled
        
scaled at center.

::

    def transform_combined(self, transform: Affine2D)

**Inherited from:** TransformMixin.transform_combined
            
Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a …

::

    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self
    
**Inherited from:** TransformMixin.translated

Translated.

::

    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self
    
**Inherited from:** TransformMixin.v_mirrored

Vertical mirrored.