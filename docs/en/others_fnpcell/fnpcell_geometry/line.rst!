Module fnpcell.geometry.line
===============================

Functions
-----------

new_line
+++++++++

::
    
    def new_line(length: float, *, step: Optional[float] = None, anchor: Anchor = Anchor.START, 
                    origin: Optional[Tuple[float, float]] = None, 
                    transform: Affine2D = Affine2D.identity()) -> Line
                    
Create a Line.

new_line_between
+++++++++++++++++

::
    
    def new_line_between(start: Tuple[float, float], end: Tuple[float, float], *, 
                            step: Optional[float] = None, transform: Affine2D = Affine2D.identity()) -> Line

Classes
----------

Line
++++++

::
    
    class Line(length: float, steps: Tuple[float, ...], anchor: Anchor, transform: Affine2D)

Line(args: Any, \*kwargs: Any)

Ancestors
____________

::
    
    FunctionCurve, TransformMixin, IUpdatable, CurveMixin, ICurve, ICurveLike, IAffineTransformable

Class variables
_________________

::
    
    var anchor: Anchor
    var length: float
    var steps: Tuple[float, ...]
    var transform: Affine2D

Static methods
_________________

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
    
    var subdevisions: Tuple[float, ...]

Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple. 
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.

Methods
________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** FunctionCurve.c_mirrored

Center mirrored.

::
    
    def curve_function(self, t: float) -> Tuple[float, float]

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** FunctionCurve.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

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