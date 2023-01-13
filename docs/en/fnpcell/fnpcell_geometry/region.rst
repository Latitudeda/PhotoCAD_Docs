Module fnpcell.geometry.region
================================

Functions
----------

new_region
+++++++++++++

::
    
    def new_region(raw_shapes: Iterable[IShape] = (), origin: Optional[Tuple[float, float]] = None, 
                    transform: Affine2D = Affine2D.identity()) -> IRegion

::
    
    def split_polygon(points: Tuple[Tuple[float, float], ...], max_points: int) -> Iterable[IShape]

Classes
--------

Region
++++++++

::
    
    class Region(*args: Any, **kwargs: Any)

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
__________

::
    
    TransformMixin, IUpdatable, IRegion, IAffineTransformable

Subclasses
____________

::
    
    fnpcell.geometry.region._ImmutableRegion

Static methods
_______________

::
    
    def boolean_and(*shape_or_regions: Union[IShape, IRegion]) -> IRegion

::
    
    def boolean_or(*shape_or_regions: Union[IShape, IRegion]) -> IRegion

::
    
    def boolean_sub(subject: Union[IShape, IRegion], /, *shape_or_regions: Union[IShape, IRegion]) -> IRegion

::
    
    def boolean_xor(*shape_or_regions: Union[IShape, IRegion]) -> IRegion

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
_____________________

::
    
    var raw_shapes: Tuple[IShape, ...]
    var shapes: Tuple[IShape, ...]

Methods
________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def merged(self) -> IRegion

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** TransformMixin.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

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