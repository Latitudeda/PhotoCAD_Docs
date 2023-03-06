Module fnpcell.geometry.euler_bend_function
=============================================

Functions
-----------

new_euler_bend
+++++++++++++++

::
    
    def new_euler_bend(*, radius_eff: Optional[float] = None, radius_min: Optional[float] = None, 
                        radians: Optional[float] = None, degrees: Optional[float] = None, 
                        p: Optional[float] = None, l_max: Optional[float] = None, 
                        origin: Optional[Tuple[float, float]] = None, 
                        transform: Affine2D = Affine2D.identity()) -> EulerBend

Create a EulerBend curve.

:param degrees central angle in degrees 
:param radius_min radius minimum 
:param radius_eff radius effective choose either radius_min(imum) or radius_eff(ective) 
:param p radio of euler spiral in whole bend, 0 < p <= 1, when p = 1, 
there's no cirular part in the bend :param l_max max length of euler spiral in half bend, 
l_max is paired with radius_min choose either p or l_max, if both absent, p = 1 is assumed.

Classes
---------

EulerBend
+++++++++++++

::
    
    class EulerBend(radius_eff: Optional[float], radius_min: Optional[float], central_angle: float, 
                    p: float, transform: Affine2D)

EulerBend(args: Any, \*kwargs: Any)

Ancestors
__________

::
    
    FunctionCurve, TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Class variables
_________________

::
    
    var central_angle: float
    var p: float
    var radius_eff: Optional[float]
    var radius_min: Optional[float]
    var transform: Affine2D

Static methods
_______________

::
    
    def p_from_l_max(l_max: float, radius_min: float, central_angle: float) -> float

::
    
    def parameters(alpha: float, p: float = 1)

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** FunctionCurve.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** FunctionCurve.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
_____________________

::
    
    var raw_end_orientations: Optional[Tuple[float, float]]

Methods
_________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** FunctionCurve.c_mirrored

Center mirrored.

::
    
    def curve_function(self, t: float) -> Tuple[float, float]

::
    
    def get_radius_eff(self) -> float

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** FunctionCurve.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, 
                radians: Optional[float] = None, origin: Optional[Tuple[float, float]] = None, 
                inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** FunctionCurve.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def sample_at(self, length: float) -> SampleInfo

**Inherited from:** FunctionCurve.sample_at

return sample info at length.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** FunctionCurve.scaled

scaled at center.

::
    
    def split_at(self, length: float) -> Tuple[ICurve, ICurve]

**Inherited from:** FunctionCurve.split_at

return two subcurve at length, if length < 0, abs(length) from end.

::
    
    def subcurve(self, start: float, end: float) -> ICurve

**Inherited from:** FunctionCurve.subcurve

return a subcurve between start and end …

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** FunctionCurve.transform_combined

Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a …

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** FunctionCurve.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** FunctionCurve.v_mirrored

Vertical mirrored.