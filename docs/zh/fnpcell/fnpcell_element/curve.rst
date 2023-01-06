Module fnpcell.element.curve
==============================

Functions
----------

::
    
    def new_curve(raw_curve: ICurve, *, stroke_width: float = 1, final_stroke_width: Optional[float] = None,
                     stroke_offset: float = 0, final_stroke_offset: Optional[float] = None,
                     taper_function: ITaperCallable = TaperFunctionLinear(), miter_limit: float = 0.5,
                     extension: Tuple[float, float] = (0, 0), end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
                     origin: Optional[Tuple[float, float]] = None, transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve

Create a curve with layer.
default stroke_width=1 default stroke_offset=0 default miter_limit=0.5.

Classes
----------

::
    
    class Curve(raw_curve: ICurve, stroke_width: float, final_stroke_width: float,
                 stroke_offset: float, final_stroke_offset: float, taper_function: ITaperCallable,
                 miter_limit: float, extension: Tuple[float, float],
                 end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]], transform: Affine2D, layer: ILayer)

Curve is Subclass of polyline.

Ancestors
++++++++++


::
    
    Polyline, Polygon, TransformMixin, IUpdatable, IPolyline, ICurvedElement, ICurved, 
    ICurveLike, IPolygon, IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Class variables
+++++++++++++++++

::
    
    var end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]]
    var extension: Tuple[float, float]
    var final_stroke_offset: float
    var final_stroke_width: float
    var layer: ILayer
    var miter_limit: float
    var raw_curve: ICurve
    var stroke_offset: float
    var stroke_width: float
    var taper_function: ITaperCallable
    var transform: Affine2D

Static methods
++++++++++++++++

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None,
                             transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Polyline.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    def transform_from_origin(origin: Optional[Tuple[float, float]] = None,
                                 transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** Polyline.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Methods
+++++++++

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Polyline.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** Polyline.h_mirrored

Horizontal mirrored

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None,
                 origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** Polyline.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *,
                 center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** Polyline.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)

**Inherited from:** Polyline.transform_combined

Returns an Affine2D that is the result of the matrix product with the given transformation. It means that the original image can be transformed by a …

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** Polyline.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** Polyline.v_mirrored

Vertical mirrored.

::
    
    def with_layer(self, layer: ILayer)