Module fnpcell.geometry.function_curve
=========================================

Classes
----------

FunctionCurve
++++++++++++++

::
    
    class FunctionCurve(*args: Any, **kwargs: Any)

Base class curve.

Ancestors
_____________

::
    
    TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Subclasses
_____________

::
    
    CompatCurve, Bezier, EulerBend, Line

Class variables
__________________

    var curve_reversed: bool
    var probe_depth: int
    var subdevisions: Tuple[float, ...]

Static methods
_________________

::

    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and the translation 
transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
_____________________

::
    
    var curve_points
    var end_orientations
    var first_point
    var last_point
    var raw_end_orientations: Optional[Tuple[float, float]]

Methods
_________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def curve_function(self, t: float) -> Tuple[float, float]

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def is_good_enough(self, s: float, e: float, depth: int) -> bool

::
    
    def is_same_grid(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> bool

::
    
    def raw_curve_points(self, start: float, end: float) -> Tuple[Tuple[float, float], ...]

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
    
    def subdivide_curve(self, s: float, e: float) -> Tuple[Tuple[float, float], ...]

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