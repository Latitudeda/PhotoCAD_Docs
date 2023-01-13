Module fnpcell.geometry.hybrid_bend
=====================================

Classes
--------

HybridBend
++++++++++++

::
    
    class HybridBend(*args: Any, **kwargs: Any)

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
___________

::
    
    TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Subclasses
___________

::
    
    CosineBend, EulerBend

Class variables
________________

::
    
    var angle_step: float
    var central_angle: float
    var l_max: float
    var radius_min: float
    var transform: Affine2D

Static methods
_______________

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
___________________

::
    
    var curve_points
    var end_orientations
    var radius_eff: float

Methods
________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def curve_curvatures(self, target: float, n: int) -> Tuple[float, ...]

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** TransformMixin.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def sample_at(self, length: float) -> SampleInfo

**Inherited from:** CurveMixin.sample_at

return sample info at length.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.scaled

scaled at center.

::
    
    def split_at(self, length: float) -> Tuple[ICurve, ICurve]

**Inherited from:** CurveMixin.split_at

return two subcurve at length, if length < 0, abs(length) from end.

::
    
    def subcurve(self, start: float, end: float) -> ICurve

**Inherited from:** CurveMixin.subcurve

return a subcurve between start and end …

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