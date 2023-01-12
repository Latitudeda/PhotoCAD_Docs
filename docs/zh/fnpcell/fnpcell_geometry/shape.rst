Module fnpcell.geometry.shape
===============================

Functions
------------

new_shape
++++++++++

::
    
    def new_shape(raw_shape_points: Iterable[Tuple[float, float]], *, 
                    origin: Optional[Tuple[float, float]] = None, 
                    transform: Affine2D = Affine2D.identity()) -> IShape

Classes
----------

Shape
+++++++

::
    
    class Shape(*args: Any, **kwargs: Any)

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
____________

::
    
    TransformMixin, IUpdatable, IShape, IAffineTransformable

Subclasses
_____________

::
    
    Box, EllipticalRing, Rect, RegularPolygon, fnpcell.geometry.shape._ImmutableShape

Class variables
_________________

::
    
    var transform: Affine2D

Static methods
________________

::
    
    def merge(shapes: Iterable[IShape]) -> IRegion

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
____________________

::
    
    var raw_shape_points: Tuple[Tuple[float, float], ...]
    var shape_points

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def offsetted(self, offset: float) -> IShape

Args
offset

    float, offset towards left if positive, towards right if negative

Returns
    A new shape. If points of the shape is clockwise, positive offset makes result shape bigger, 
    negative offset makes result shape smaller. If points of the shape is counter-clockwise, 
    positive offset makes result shape smaller, negative offset makes result shape bigger.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

Inherited from: TransformMixin.rotated

Return a new cell reference rotated, either degrees or radians must be provided. If both provided, radians is used …

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