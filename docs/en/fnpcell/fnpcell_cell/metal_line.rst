Module fnpcell.cell.metal_line
================================

Classes
---------

::

    class MetalLine(cell: ICell, raw_curve: ICurve, type: IMetalLineType,
                     offset: float = 0, final_offset: Optional[float] = None,
                     extension: Tuple[float, float] = (0, 0), transform: Affine2D = Affine2D.identity(),
                     patches: Tuple[IElement, ...] = (), name: str = 'wg')

MetalLine is for defining a MetalLine.
Any modification will create new MetalLine instead of modify the original MetalLine.

Ancestors
+++++++++++

::

    IMetalLineLike, ICurveLike, ICurvedCellRef, ICurved, CellRef, 
    TransformMixin, ICellRef, IUpdatable, IElement, IRunnable, IAffineTransformable

Class variables
++++++++++++++++

::

    var cell: ICell
    var extension: Tuple[float, float]
    var final_offset: Optional[float]
    var name: str
    var offset: float
    var patches: Tuple[IElement, ...]
    var raw_curve: ICurve
    var transform: Affine2D
    var type: IMetalLineType

Static methods
+++++++++++++++

::

    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None,
                             transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** CellRef.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None,
                                 transform: Affine2D = Affine2D.identity()) -> Affine2D
        
**Inherited from:** CellRef.transform_from_origin
            
Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, It …

Instance variables
+++++++++++++++++++++

::

    var curve_length: float
        
Return curve length.

::
    
    var ports

**Inherited from:** CellRef.ports

Return owned ports of the cell reference.

Methods
++++++++

::

    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self
        
**Inherited from:** IMetalLineLike.c_mirrored

Center mirrored.

::
    
    def content_merged(self, *, affected_layer: Iterable[ILayer])

**Inherited from:** CellRef.content_merged

Return a new cell reference with close elements on same layer merged into polygons. 
Multiple layers can be provided and elements on each layer will be …

::
    
    def flatten(self, depth: int = 1)

**Inherited from:** CellRef.flatten

Return a new cell reference with transformed content and identity transform to itself. 
Useful to fix the "1nm gap" due to gds spec This method only …

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IMetalLineLike.h_mirrored

Horizontal mirrored

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1,
                     row_height: float = 0, transform: Affine2D = Affine2D.identity())

**Inherited from:** CellRef.new_array

Return a new cell reference array

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None,
                 origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self
        
**Inherited from:** IMetalLineLike.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, center: Tuple[float, float] = (0, 0)) -> ~_Self
        
**Inherited from:** IMetalLineLike.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)
        
**Inherited from:** CellRef.transform_combined

Return a new cell reference with a new transform which is its transform combined with the given transform

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self
        
**Inherited from:** IMetalLineLike.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self
        
**Inherited from:** IMetalLineLike.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self, bands: Optional[Iterable[IBand]])
        
**Inherited from:** IMetalLineLike.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self, name: str)
        
**Inherited from:** IMetalLineLike.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self, content: Iterable[IElement])
        
**Inherited from:** IMetalLineLike.with_patches
            
If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self, ports: Sequence[Union[None, str, Hidden]])
        
**Inherited from:** IMetalLineLike.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …