Module fnpcell.element.polygon_set
====================================

Functions
----------

::
    
    def new_polygon_set(raw_region: Union[IRegion, Iterable[IPolygon]], /, *, layer: ILayer,
                         origin: Optional[Tuple[float, float]] = None,
                         transform: Affine2D = Affine2D.identity()) -> IPolygonSet

Classes
--------

::
    
    class PolygonSet(*args: Any, **kwargs: Any)

Interface of element,element is geometry with layer.

Ancestors
++++++++++

::
    
    TransformMixin, IUpdatable, IPolygonSet, IPrimitive, 
    ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
+++++++++++

::
    
    fnpcell.element.polygon_set._ImmutablePolygonSet

Class variables
+++++++++++++++++

::
    
    var polygons: Tuple[IPolygon, ...]
    var region: IRegion

Static methods
+++++++++++++++

::
    
    def boolean_and(*operands: Union[IPolygon, IPolygonSet], layer: ILayer) -> IPolygonSet

::
    
    def boolean_or(*operands: Union[IPolygon, IPolygonSet], layer: ILayer) -> IPolygonSet

::
    
    def boolean_sub(subject: Union[IPolygon, IPolygonSet], /, *operands: Union[IPolygon, IPolygonSet],
                     layer: ILayer) -> IPolygonSet

::
    
    def boolean_xor(*operands: Union[IPolygon, IPolygonSet], layer: ILayer) -> IPolygonSet

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

Methods
++++++++

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def inverted(self, bounding_shape: IShape) -> IPolygonSet

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

::
    
    def with_layer(self, layer: ILayer)