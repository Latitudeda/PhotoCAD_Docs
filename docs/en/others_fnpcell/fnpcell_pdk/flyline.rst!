Module fnpcell.pdk.flyline
=============================

Classes
---------

Flyline
+++++++++

::
    
    class Flyline(start: ITerminal, end: ITerminal, waypoints: Tuple[Tuple[float, float], ...], 
                    layer: ILayer, port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]], 
                    stroke_width: float = 0.5, transform: Affine2D = Affine2D.identity(), 
                    patches: Tuple[IElement, ...] = (), name: str = 'flyline')

Flyline(start: fnpcell.interfaces.ITerminal, end: fnpcell.interfaces.ITerminal, 
waypoints: Tuple[Tuple[float, float], …], layer: fnpcell.interfaces.ILayer, 
port_names: Tuple[Union[NoneType, str, fnpcell.interfaces.Hidden], 
Union[NoneType, str, fnpcell.interfaces.Hidden]], stroke_width: float = 0.5, 
transform: fnpcell.transform.Affine2D = Affine2D.identity(), 
patches: Tuple[fnpcell.interfaces.IElement, …] = (), name: str = 'flyline')

Ancestors
___________

::
    
    CellRef, TransformMixin, ICurvedCellRef, ICurved, ICellRef, IUpdatable, IElement, 
    IRunnable, IAffineTransformable, ICurveLike

Class variables
_________________

::
    
    var end: ITerminal
    var layer: ILayer
    var name: str
    var patches: Tuple[IElement, ...]
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]
    var start: ITerminal
    var stroke_width: float
    var transform: Affine2D
    var waypoints: Tuple[Tuple[float, float], ...]

Static methods
_________________

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

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
____________________

::
    
    var cell: ICell
    var curve_length: float
    var ports

**Inherited from:** CellRef.ports

Return owned ports of the cell reference.

::
    
    var raw_curve: ICurve

Methods
___________

::

    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** CellRef.c_mirrored

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

**Inherited from:** CellRef.h_mirrored

Horizontal mirrored.

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1, row_height: float = 0, 
                    transform: Affine2D = Affine2D.identity())

**Inherited from:** CellRef.new_array

Return a new cell reference array.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, 
                radians: Optional[float] = None, origin: Optional[Tuple[float, float]] = None, 
                inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** CellRef.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** CellRef.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** CellRef.transform_combined

Return a new cell reference with a new transform which is its transform 
combined with the given transform.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** CellRef.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** CellRef.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self, bands: Optional[Iterable[IBand]])

Add bands.

::
    
    def with_name(self, name: str)

Return a new cell with the given name.

::
    
    def with_patches(self, content: Iterable[IElement])

Add content.

::
    
    def with_ports(self, ports: Sequence[Union[None, str, Hidden]])

Return a new cell with the given ports.