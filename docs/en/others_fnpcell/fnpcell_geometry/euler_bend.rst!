Module fnpcell.geometry.euler_bend
====================================

Functions
-----------

new_euler_bend
+++++++++++++++++

::
    
    def new_euler_bend(*, radius_min: float, radians: Optional[float] = None, 
                        degrees: Optional[float] = None, p: Optional[float] = None, 
                        l_max: Optional[float] = None, angle_step: Optional[float] = None, 
                        origin: Optional[Tuple[float, float]] = None, 
                        transform: Affine2D = Affine2D.identity()) -> EulerBend

Create a EulerBend curve.

:param degrees central angle in degrees :param radius_min radius minimum 
:param radius_eff radius effective choose either radius_min(imum) or radius_eff(ective) 
:param p radio of euler spiral in whole bend, 0 < p <= 1, when p = 1, there's no cirular part in the bend 
:param l_max max length of euler spiral in half bend, l_max is paired with radius_min choose either p or l_max, 
if both absent, p = 1 is assumed.

Classes
---------

EulerBend
++++++++++

::
    
    class EulerBend(radius_min: float, central_angle: float, l_max: float, angle_step: float, 
                    transform: Affine2D = Affine2D.identity())

EulerBend(args: Any, \*kwargs: Any)

Ancestors
___________

::
    
    HybridBend, TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Class variables
_________________

::
    
    var angle_step: float
    var central_angle: float
    var l_max: float
    var radius_min: float
    var transform: Affine2D

Static methods
_________________

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** HybridBend.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** HybridBend.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** HybridBend.c_mirrored

Center mirrored.

::
    
    def curve_curvatures(self, target: float, n: int)

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** HybridBend.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** HybridBend.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def sample_at(self, length: float) -> SampleInfo

**Inherited from:** HybridBend.sample_at

return sample info at length.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** HybridBend.scaled

scaled at center.

::
    
    def split_at(self, length: float) -> Tuple[ICurve, ICurve]

**Inherited from:** HybridBend.split_at

return two subcurve at length, if length < 0, abs(length) from end.

def subcurve(self, start: float, end: float) -> ICurve

**Inherited from:** HybridBend.subcurve

return a subcurve between start and end …

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** HybridBend.transform_combined

Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a …

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** HybridBend.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** HybridBend.v_mirrored

Vertical mirrored.