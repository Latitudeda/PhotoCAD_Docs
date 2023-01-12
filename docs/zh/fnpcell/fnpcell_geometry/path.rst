Module fnpcell.geometry.path
=============================

Classes
---------

Path
++++++

::
    
    class Path(breakpoints: Tuple[Tuple[float, float], ...], curves: Tuple[Tuple[ICurve, bool], ...], 
                transform: Affine2D = Affine2D.identity())

Path(args: Any, \*kwargs: Any)

Ancestors
_____________

::
    
    TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Class variables
_________________

::
    
    var breakpoints: Tuple[Tuple[float, float], ...]
    var curves: Tuple[Tuple[ICurve, bool], ...]
    var transform: Affine2D

Static methods
________________

::
    
    def move(*, to: Tuple[float, float] = (0, 0)) -> Path

Create a Path.

::
    
    def smooth(waypoints: Iterable[Tuple[float, float]], *, bend_factory: IBendCurveFactory) -> Path

::
    
    def stubbed(waypoints: Iterable[Tuple[float, float]], *, stub_width: float, 
                stub_right_angle: bool = False) -> Path

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
______________________

::
    
    var curve_points
    var end_orientations
    var first_point
    var last_point

Methods
_________

::
    
    def appended(self, curve: ICurve, end_at: Optional[Tuple[float, float]] = None, reverse: bool = False)

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def close(self, *, step: Optional[float] = None) -> Path

::
    
    def cubic_bezier(self, *, to: Tuple[float, float], control1: Optional[Tuple[float, float]] = None, 
                        control2: Tuple[float, float]) -> Path

::
    
    def elliptical_arc(self, *, to: Tuple[float, float], radius: Union[float, Iterable[float]], 
                        rotation: float = 0, large_arc: bool = False, clockwise: bool = False) -> Path

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def line(self, *, to: Tuple[float, float], step: Optional[float] = None) -> Path

::
    
    def quadratic_bezier(self, *, to: Tuple[float, float], control: Optional[Tuple[float, float]] = None) -> Path

::
    
    def ray(self, *, orientation: float, length: float, step: Optional[float] = None) -> Path

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
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

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