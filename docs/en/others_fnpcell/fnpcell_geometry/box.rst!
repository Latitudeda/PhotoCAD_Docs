Module fnpcell.geometry.box
=============================

Functions
-----------

new_box
++++++++++

::
    
    def new_box(*, width: float, height: float, stroke_width: float = 1, 
                origin: Optional[Tuple[float, float]] = None, 
                transform: Affine2D = Affine2D.identity()) -> Box

Create a box.

Classes
----------

box
+++++

::
    
    class Box(width: float, height: float, stroke_width: float, transform: Affine2D)

Box(args: Any, \*kwargs: Any)

Ancestors
__________

::
    
    Shape, TransformMixin, IUpdatable, IShape, IAffineTransformable

Class variables
_________________

::
    
    var height: float
    var stroke_width: float
    var transform: Affine2D
    var width: float

Static methods
________________

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Shape.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Shape.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, It …

Instance variables
_____________________

::
    
    var raw_shape_points : Tuple[Tuple[float, float], ...]

Return all points of box

Methods
_________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Shape.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** Shape.h_mirrored

Horizontal mirrored.

::
    
    def offsetted(self, offset: float) -> IShape

**Inherited from:** Shape.offsetted

    Args
    offset

        float, offset towards left if positive, towards right if negative …

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** Shape.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Shape.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** Shape.transform_combined

Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a …

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** Shape.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** Shape.v_mirrored

Vertical mirrored.