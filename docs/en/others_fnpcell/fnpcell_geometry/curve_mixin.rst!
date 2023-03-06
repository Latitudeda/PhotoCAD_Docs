Module fnpcell.geometry.curve_mixin
=====================================

Classes
--------

CurveMixin
++++++++++++

::
    
    class CurveMixin(*args: Any, **kwargs: Any)

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
__________

::
    
    ICurve, ICurveLike, IAffineTransformable

Subclasses
___________

::
    
    EllipticalArc, FunctionCurve, HybridBend, Path, Polyline

Class variables
__________________

::
    
    var transform: Affine2D

Static methods
________________

::
    
    def correct_ends(points: Sequence[Tuple[float, float]], 
                        end_orientations: Tuple[float, float]) -> Tuple[Tuple[float, float], ...]

Instance variables
____________________

::
    
    var alengths

Methods
________

::
    
    def bundle(self, *, size: int, spacing: float, final_spacing: Optional[float] = None, 
                offset: float = 0, final_offset: Optional[float] = None, 
                taper_function: ITaperCallable = TaperFunctionLinear()) -> Tuple[ICurve, ...]

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurve.c_mirrored

Center mirrored.

::
    
    
    def extended(self, extension: Tuple[float, float] = (0, 0), 
                    end_orientations: Optional[Tuple[float, float]] = None) -> ICurve

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurve.h_mirrored

Horizontal mirrored.

::
    
    def offsetted(self, offset: float, miter_limit: float = inf, final_offset: Optional[float] = None, 
                    taper_function: ITaperCallable = TaperFunctionLinear())

::
    
    def rail(self, width: float, *, offset: float = 0, miter_limit: float = 0.5, 
                final_width: Optional[float] = None, final_offset: Optional[float] = None, 
                taper_function: ITaperCallable = TaperFunctionLinear()) -> Tuple[ICurve, ICurve]

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurve.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def sample_at(self, length: float) -> SampleInfo

**Inherited from:** ICurve.sample_at

return sample info at length.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurve.scaled

scaled at center.

::
    
    def split_at(self, length: float) -> Tuple[ICurve, ICurve]

**Inherited from:** ICurve.split_at

return two subcurve at length, if length < 0, abs(length) from end.

::
    
    def subcurve(self, start: float, end: float) -> ICurve

**Inherited from:** ICurve.subcurve

return a subcurve between start and end …

::
    
    def to_shape(self) -> IShape

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurve.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurve.v_mirrored

Vertical mirrored.