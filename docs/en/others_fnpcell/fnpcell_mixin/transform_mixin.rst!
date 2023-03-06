Module fnpcell.mixin.transform_mixin
======================================

Classes
----------

TransformMixin
+++++++++++++++++

::
    
    class TransformMixin

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
____________

::
    
    IUpdatable IAffineTransformable

Subclasses
____________

::
    
    CellArray, CellRef, Composite, DataMatrixCode, Group, Label, Polygon, PolygonSet, 
    QRCode, Text, EllipticalArc, FunctionCurve, HybridBend, Path, Polyline, Region, Shape

Class variables
___________________

::
    
    var transform: Affine2D

Static methods
___________________

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the origin can be passed in as Point2D, IPositioned, 
and IRay with coordinate attributes. It means that the original image can be transformed around this 
given origin, such as scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

Returns an Affine2D that is the result of the matrix product of the given 
transformation and the translation transformation at the given origin, 
It means that the original image can be transformed around this given origin, 
such as scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Methods
____________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IAffineTransformable.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a composite transformation matrix, 
which can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.