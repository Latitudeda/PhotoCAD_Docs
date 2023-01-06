Module fnpcell.element.polyline
=================================

Functions
----------

::
    
    def new_polyline(raw_polyline_points: Iterable[Tuple[float, float]], *,
                     stroke_width: float = 1, final_stroke_width: Optional[float] = None,
                     stroke_offset: float = 0, final_stroke_offset: Optional[float] = None,
                     taper_function: ITaperCallable = TaperFunctionLinear(),
                     raw_end_orientations: Optional[Tuple[float, float]] = None,
                     miter_limit: float = 0.5, extension: Tuple[float, float] = (0, 0),
                     end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
                     origin: Optional[Tuple[float, float]] = None,
                     transform: Affine2D = Affine2D.identity(), layer: ILayer) -> IPolyline

Create a polyline with layer.

Classes
----------

::
    
    class Polyline(*args: Any, **kwargs: Any)

Polygon is a class for defining a polygon.

Ancestors
+++++++++++++

::
    
    Polygon, TransformMixin, IUpdatable, IPolyline, ICurved, ICurveLike, IPolygon, 
    IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
++++++++++++

::
    
    Curve fnpcell.element.polyline._ImmutablePolyline

Class variables
+++++++++++++++++

::
    
    var end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]]
    var extension: Tuple[float, float]
    var final_stroke_offset: float
    var final_stroke_width: float
    var miter_limit: float
    var stroke_offset: float
    var stroke_width: float
    var taper_function: ITaperCallable

Static methods
++++++++++++++++

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None,
                             transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Polygon.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None,
                                 transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Polygon.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
+++++++++++++++++++

::
    
    var alengths
    var curve_length: float
    var end_rays
    var polygon_points
    var polyline_curve
    var polyline_points: Tuple[Tuple[float, float], ...]
    var shape: IShape

Methods
++++++++

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Polygon.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** Polygon.h_mirrored

Horizontal mirrored.

::
    
    def polyline_preconditions(self) -> None

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None,
                 origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** Polygon.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *,
                 center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Polygon.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** Polygon.transform_combined

Returns an Affine2D that is the result of the matrix product with the given transformation. 
It means that the original image can be transformed by a …

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** Polygon.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** Polygon.v_mirrored

Vertical mirrored.