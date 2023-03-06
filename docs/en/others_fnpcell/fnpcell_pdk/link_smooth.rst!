Module fnpcell.pdk.link_smooth
================================

Functions
----------

new_link_smooth
++++++++++++++++

::
    
    def new_link_smooth(route: Iterable[Tuple[float, float]], *, 
                        name: str = 'LinkSmooth', link_type: IWaveguideType, 
                        bend_factory: IBendWaveguideFactory, 
                        straight_factory: Optional[IStraightWaveguideFactory] = None, 
                        start_type: Optional[IWaveguideType] = None, 
                        end_type: Optional[IWaveguideType] = None, 
                        target_length: Optional[float] = None, 
                        ports: Sequence[Union[None, str, Hidden]] = ('op_0', 'op_1'), 
                        auto_transition: Optional[AutoTransition] = None, 
                        transform: Affine2D = Affine2D.identity()) -> LinkSmooth

Classes
--------

LinkSmooth
++++++++++++

::
    
    class LinkSmooth(control_points: Tuple[Tuple[float, float], ...], 
                        link_type: IWaveguideType, straight_factory: IStraightWaveguideFactory, 
                        bend_factory: IBendWaveguideFactory, transform: Affine2D, 
                        name: str = 'LinkSmooth', start_type: Optional[IWaveguideType] = None, 
                        end_type: Optional[IWaveguideType] = None, 
                        port_names: Sequence[Union[None, str, Hidden]] = ('op_0', 'op_1'), 
                        auto_transition: Optional[AutoTransition] = None, 
                        bands: Optional[FrozenSet[IBand]] = None, patches: Tuple[IElement, ...] = ())

Ancestors
_____________

::
    
    ILink, IWaveguideLike, ICurveLike, ICurvedCellRef, ICurved, CellRef, TransformMixin, ICellRef, 
    IUpdatable, IElement, IRunnable, IAffineTransformable

Class variables
__________________

::
    
    var auto_transition: Optional[AutoTransition]
    var bands: Optional[FrozenSet[IBand]]
    var bend_factory: IBendWaveguideFactory
    var control_points: Tuple[Tuple[float, float], ...]
    var end_type: Optional[IWaveguideType]
    var link_type: IWaveguideType
    var name: str
    var patches: Tuple[IElement, ...]
    var port_names: Sequence[Union[None, str, Hidden]]
    var start_type: Optional[IWaveguideType]
    var straight_factory: IStraightWaveguideFactory
    var transform: Affine2D

Static methods
__________________

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
___________________

::
    
    var cell: ICell
    var ports

**Inherited from:** CellRef.ports

Return owned ports of the cell reference.

::
    
    var raw_curve: ICurve

Methods
_________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILink.c_mirrored

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

**Inherited from:** ILink.h_mirrored

Horizontal mirrored.

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1, row_height: float = 0, t
                    ransform: Affine2D = Affine2D.identity())

**Inherited from:** CellRef.new_array

Return a new cell reference array.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ILink.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) > ~_Self

**Inherited from:** ILink.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** CellRef.transform_combined

Return a new cell reference with a new transform which is its transform combined with the given transform.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ILink.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ILink.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self, bands: Optional[Iterable[IBand]])

**Inherited from:** ILink.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self, name: str)

**Inherited from:** ILink.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self, content: Iterable[IElement])

**Inherited from:** ILink.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self, ports: Sequence[Union[None, str, Hidden]])

**Inherited from:** ILink.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …