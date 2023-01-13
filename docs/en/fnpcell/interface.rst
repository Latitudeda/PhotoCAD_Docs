fnpcell.interfaces
===========================

Common interfaces and value types for fnpcell

Functions
-----------

Waypoint
++++++++++

::
    
    def Waypoint(x: float, y: float, a: float) -> IRay

Create a Waypoint.

x,y is location. a is angle in degrees.

angle_between
+++++++++++++++

::
    
    def angle_between(point: Tuple[float, float], 
                        origin: Tuple[float, float] = (0, 0)) -> float

Return angle in radians.

cache
++++++

::
    
    def cache() -> Callable[[~_Fn], ~_Fn]

Used as cache decorator.

Arguments to the cached function must be hashable.

clamp
++++++

::
    
    def clamp(value: float, min: float, max: float)

Return value :math:`\in` [min, max]. 

distance_between
++++++++++++++++++

::
    
    def distance_between(point: Tuple[float, float], 
                            origin: Tuple[float, float] = (0, 0)) -> float

Return distance between point and origin.

is_abstract
++++++++++++

::
    
    def is_abstract(cls: Type[Any])

Determine whether cls is a abstract class.

is_dataclass
+++++++++++++++++

::
    
    def is_dataclass(cls: Type[Any]) -> bool

midpoint_of
+++++++++++++

::
    
    def midpoint_of(point: Tuple[float, float], 
                    origin: Tuple[float, float] = (0, 0)) -> Tuple[float, float]

Return middle point of point and origin.

normalize_angle
+++++++++++++++++

::
    
    def normalize_angle(angle: float) -> float

Return angle :math:`\in` [-math.pi, math.pi].

transform_between
+++++++++++++++++++

::
    
    def transform_between(device: IPositioned, host: IPositioned) -> Affine2D

Return transform from device to host.

Classes
---------

Absolute
+++++++++

::
    
    class Absolute(value: float)

Absolute(value: float)

Class variables
_________________

::
    
    var value: float

Anchor
++++++++

::
    
    class Anchor(value, names=None, *, module=None, qualname=None, type=None, start=1)

Assign where the (0, 0) is.

Usage
_______

from fnpcell import all as fp Straight(name="", anchor=fp.Anchor.CENTER, …)

Ancestors
____________

::
    
    enum.Enum

Class variables
__________________

::
    
    var CENTER
    var END
    var START

FrozenDict
++++++++++++

::
    
    class FrozenDict(*args: Any, **kwargs: Any)

An immutable dict which supports hashing.

Ancestors
___________

::
    
    collections.abc.Mapping, collections.abc.Collection, collections.abc.Sized, collections.abc.Iterable, 
    collections.abc.Container, typing.Generic

Static methods
________________

::
    
    def freeze(value: Any) -> Any

Methods
__________

::
    
    def get(self, key: ~_K, default: Optional[~_V] = None)

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

Glyph
++++++

::
    
    class Glyph(advance_width: float, left_side_bearing: float, right_side_bearing: float, 
                bounding_box: Tuple[Tuple[float, float], Tuple[float, float]], 
                highlight_box: Tuple[Tuple[float, float], Tuple[float, float]], 
                paths: Tuple[Tuple[Union[Tuple[Literal['Z']], Tuple[Literal['L', 'M'], 
                Tuple[float, float]], Tuple[Literal['Q'], Tuple[float, float], 
                Tuple[float, float]], Tuple[Literal['C'], Tuple[float, float], 
                Tuple[float, float], Tuple[float, float]]], ...], ...])

Glyph(advance_width: float, left_side_bearing: float, right_side_bearing: float, 
bounding_box: Tuple[Tuple[float, float], Tuple[float, float]], 
highlight_box: Tuple[Tuple[float, float], Tuple[float, float]], 
paths: Tuple[Tuple[Union[Tuple[Literal['Z']], Tuple[Literal['L', 'M'], 
Tuple[float, float]], Tuple[Literal['Q'], Tuple[float, float], 
Tuple[float, float]], Tuple[Literal['C'], Tuple[float, float], 
Tuple[float, float], Tuple[float, float]]], …], …])

Class variables
__________________

::
    
    var advance_width: float
    var bounding_box: Tuple[Tuple[float, float], Tuple[float, float]]
    var highlight_box: Tuple[Tuple[float, float], Tuple[float, float]]
    var left_side_bearing: float

    var paths: Tuple[Tuple[Union[Tuple[Literal['Z']], Tuple[Literal['L', 'M'], 
    Tuple[float, float]], Tuple[Literal['Q'], Tuple[float, float], 
    Tuple[float, float]], Tuple[Literal['C'], Tuple[float, float], 
    Tuple[float, float], Tuple[float, float]]], ...], ...]

    var right_side_bearing: float

Hidden
++++++++

::
    
    class Hidden(name: str)

Hidden(name: str).

Class variables
_________________

::
    
    var name: str

IAffineTransformable
++++++++++++++++++++++

::
    
    class IAffineTransformable

IAffineTransformable supports transform, can be scaled, rotated, translated, 
h_mirrored, v_mirrored, c_mirrored.

Subclasses
___________

::
    
    ICurve, ICurved, IElement, IRegion, IShape, TransformMixin

Class variables
__________________

::
    
    var transform: Affine2D

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used.

Rotation origin can be provided too.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

scaled at center.

::
    
    def transform_combined(self: ~_Self, transform: Affine2D) -> ~_Self

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

Vertical mirrored.

IAutoVias
+++++++++++

::
    
    class IAutoVias

Subclasses
____________

::
    
    AutoVias

IBand
++++++++

::
    
    class IBand

Interface of Band type.

Subclasses
_____________
::
    
    Band

Class variables
_________________

::
    
    var name: str

IBendCurveFactory
+++++++++++++++++++

::
    
    class IBendCurveFactory(*args, **kwargs)

Base class for protocol classes.

Protocol classes are defined as::
    
    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize structural 
subtyping (static duck-typing), for example::
    
    class C:
        def meth(self) -> int:
            return 0

        def func(x: Proto) -> int:
            return x.meth()

        func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with @typing.runtime_checkable act as simple-minded 
runtime protocols that check only the presence of given attributes, ignoring their type signatures. 
Protocol classes can be generic, they are defined as::
    
    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...

Ancestors
__________

::
    
    typing.Protocol, typing.Generic

IBendWaveguideFactory
+++++++++++++++++++++++

::
    
    class IBendWaveguideFactory(*args, **kwargs)

Base class for protocol classes.

Protocol classes are defined as::
    
    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize structural 
subtyping (static duck-typing), for example::
    
    class C:
        def meth(self) -> int:
            return 0

        def func(x: Proto) -> int:
             return x.meth()

        func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with @typing.runtime_checkable act as 
simple-minded runtime protocols that check only the presence of given attributes, 
ignoring their type signatures. Protocol classes can be generic, they are defined as::
    
    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...

Ancestors
___________

::
    
    typing.Protocol, typing.Generic

ICell
++++++++

::
    
    class ICell(*args, **kwds)

Super class of containers. An IRunnableContainer runs processors to process itself and its content.

Ancestors
____________

::
    
    IUpdatable, IRunnableContainer, typing.Generic, IRunnable

Subclasses
____________

::
    
    fnpcell.cell.cell._CellMixin, fnpcell.cell.cell._PatchedCell

Class variables
__________________

::
    
    var bands: Optional[FrozenSet[IBand]]
    var content: Tuple[IElement, ...]
    var name: Optional[str]
    var ports: Tuple[ITerminal, ...]

Methods
__________

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1, 
                    row_height: float = 0, transform: Affine2D = Affine2D.identity()) -> ICellArray

::
    
    def new_ref(self, transform: Affine2D = Affine2D.identity()) -> ICellRef

::
    
    def polygon_set(self, *, layer: ILayer, union: bool = True) -> IPolygonSet

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

::
    
    def with_content(self: ~_Self, content: Iterable[IElement]) -> ~_Self

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

ICellArray
++++++++++++

::
    
    class ICellArray

Interface of element,element is geometry with layer.

Ancestors
___________

::
    
    IElement, IRunnable, IAffineTransformable

Subclasses
___________

::
    
    CellArray

Class variables
_________________

::
    
    var cell: ICell
    var col_end: Tuple[float, float]
    var cols: int
    var row_end: Tuple[float, float]
    var rows: int
    var transform: Affine2D

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.c_mirrored

Center mirrored.

::
    
    def decompose(self) -> Tuple[ICellRef, ...]

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IElement.h_mirrored

Horizontal mirrored.

::
    
    def polygon_set(self, *, layer: ILayer, union: bool = True) -> IPolygonSet

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IElement.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                enter: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IElement.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IElement.v_mirrored

Vertical mirrored.

ICellRef
+++++++++

::
    
    class ICellRef

Interface of CellRef.

Ancestors
____________

::
    
    IUpdatable, IElement, IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    CellRef, ICurvedCellRef, fnpcell.pdk._pcell_runtime._Proxy

Class variables
__________________

::
    
    var cell: ICell
    var transform: Affine2D

Instance variables
_____________________

::
    
    var ports: Tuple[IOwnedTerminal, ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.c_mirrored

Center mirrored.

::
    
    def content_merged(self: ~_Self, *, affected_layer: Iterable[ILayer]) -> ~_Self

::
    
    def flatten(self, depth: int = 1) -> ICell

::
    
    def frozen(self: ~_Self) -> ~_Self

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IElement.h_mirrored

Horizontal mirrored.

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1, 
                    row_height: float = 0, transform: Affine2D = Affine2D.identity()) -> ICellArray

::
    
    def polygon_set(self, *, layer: ILayer, union: bool = True) -> IPolygonSet\

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, 
                radians: Optional[float] = None, origin: Optional[Tuple[float, float]] = None, 
                inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IElement.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**nherited from:** IElement.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IElement.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, returns a new object with the given bands, 
which is used to modify the bands attribute.

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, returns a new object with the given name, 
which is used to modify the name attribute.

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, returns a new object with the given content, 
which is used to modify the patches attribute.

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, returns a new object with the given ports, 
which is used to modify the ports attribute.

IComposite
++++++++++++

::
    
    class IComposite(*args, **kwds)

Super class of containers. An IRunnableContainer runs processors to process itself and its content.

Ancestors
___________

::
    
    IRunnableContainer, typing.Generic, IElement, IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    fnpcell.cell.composite._CompositeMixin

Class variables
________________

::
    
    var content: Tuple[IElement, ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.c_mirrored

Center mirrored.

::
    
    def flatten(self, depth: int = 1) -> Tuple[IElement, ...]

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IElement.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IElement.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IElement.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self
    
**Inherited from:** IElement.v_mirrored

Vertical mirrored.

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

::
    
    def with_ports(self, *ports: ITerminal) -> ICell

ICurve
+++++++++    

::
    
    class ICurve

IAffineTransformable supports transform, can be scaled, rotated, translated, 
h_mirrored, v_mirrored, c_mirrored.

Ancestors
___________

::
    
    ICurveLike. IAffineTransformable

Subclasses
____________

::
    
    CurveMixin

Class variables
_________________

::
    
    var transform: Affine2D

Instance variables
_____________________

::
    
    var curve_length
    var curve_points: Tuple[Tuple[float, float], ...]
    var end_orientations: Tuple[float, float]
    var end_rays
    var first_point: Tuple[float, float]
    var last_point: Tuple[float, float]

Methods
__________

::
    
    def bundle(self, *, size: int, spacing: float, final_spacing: Optional[float] = None, 
                offset: float = 0, final_offset: Optional[float] = None, 
                taper_function: ITaperCallable = TaperFunctionLinear()) -> Tuple[ICurve, ...]

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.c_mirrored

Center mirrored.

::
    
    def extended(self, extension: Tuple[float, float] = (0, 0), 
                    end_orientations: Optional[Tuple[float, float]] = None) -> ICurve

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.h_mirrored

Horizontal mirrored.

::
    
    def offsetted(self, offset: float, final_offset: Optional[float] = None, miter_limit: float = inf, 
                    taper_function: ITaperCallable = TaperFunctionLinear()) -> ICurve

::
    
    def rail(self, width: float, *, offset: float = 0, miter_limit: float = 0.5, 
                final_width: Optional[float] = None, final_offset: Optional[float] = None, 
                taper_function: ITaperCallable = TaperFunctionLinear()) -> Tuple[ICurve, ...]

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IAffineTransformable.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def sample_at(self, length: float) -> SampleInfo

return sample info at length.

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.scaled

scaled at center.

::
    
    def split_at(self, length: float) -> Tuple[ICurve, ICurve]

return two subcurve at length, if length < 0, abs(length) from end.

::
    
    def subcurve(self, start: float, end: float) -> ICurve

return a subcurve between start and end.

start: start position in length from start end: end position in length from start. 
If negative, calculate from end

::
    
    def to_shape(self) -> IShape

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.

ICurveLike
++++++++++++

::
    
    class ICurveLike

Subclasses
________________

::
    
    ICurve, ILink, IMetalLineLike, IPolyline, IWaveguideLike, Flyline

Instance variables
_____________________

::
    
    var curve_length: float

ICurvePaint
++++++++++++

::
    
    class ICurvePaint(*args, **kwargs)

Base class for protocol classes.

Protocol classes are defined as::
    
    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize structural 
subtyping (static duck-typing), for example::
    
    class C:
        def meth(self) -> int:
            return 0

        def func(x: Proto) -> int:
            return x.meth()

        func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with @typing.runtime_checkable act as simple-minded 
runtime protocols that check only the presence of given attributes, ignoring their type signatures. 
Protocol classes can be generic, they are defined as::
    
    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...

Ancestors
___________

::
    
    typing.Protocol, typing.Generic

Subclasses
____________

::
    
    CompositeCurvePaint, ContinuousLayerCurvePaint, PeriodicSamplingCurvePaint

ICurved
+++++++++

::
    
    class ICurved

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
____________

::
    
    IAffineTransformable

Subclasses
____________

::
    
    ICurvedCellRef, ICurvedElement, IPolyline

Class variables
_____________________

::
    
    var raw_curve: ICurve

Instance variables
_____________________

::
    
    var curve

Methods
__________

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
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.

ICurvedCellRef
++++++++++++++++

::
    
    class ICurvedCellRef

Interface of CellRef.

Ancestors
___________

::
    
    ICurved, ICellRef, IUpdatable, IElement, IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    fnpcell.cell.cell_ref._ImmutableCurvedCellRef, ILink, IMetalLineLike, IWaveguideLike, Flyline

Class variables
________________

::
    
    var raw_curve: ICurve

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurved.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurved.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurved.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurved.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ICellRef.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ICellRef.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ICellRef.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ICellRef.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

ICurvedElement
+++++++++++++++++

::
    
    class ICurvedElement

Interface of element,element is geometry with layer.

Ancestors
___________

::
    
    ICurved, IElement, IRunnable, IAffineTransformable

Subclasses
___________

::
    
    Curve

Class variables
_________________

::
    
    var raw_curve: ICurve

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurved.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurved.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurved.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurved.v_mirrored

Vertical mirrored.

IElectronicMaterial
+++++++++++++++++++++

::
    
    class IElectronicMaterial

Ancestors
_____________

::
    
    IMaterial

Class variables
__________________

::
    
    var name: str

IElement
++++++++++++   

::
    
    class IElement

Interface of element,element is geometry with layer.

Ancestors
___________

::
    
    IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    ICellArray, ICellRef, IComposite, ICurvedElement, IPrimitive

Class variables
__________________

::
    
    var transform: Affine2D

Methods
__________

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
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.

IFont
_______

::
    
    class IFont

Attributes
________________

::
    
    name

global unique name for the font, used for hash and eq.

Class variables
________________

::
    
    var ascender: float
    var descender: float
    var glyphs: Mapping[str, Glyph]
    var name: str
    var units_per_em: float

IGroup
++++++++

::
    
    class IGroup(*args, **kwds)

Super class of containers. An IRunnableContainer runs processors to process itself and its content.

Ancestors
___________

::
    
    IRunnableContainer, typing.Generic, IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
____________

::
    
    DataMatrixCode, Group, Label, QRCode

Class variables
________________

::
    
    var content: Tuple[IPrimitive, ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IPrimitive.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IPrimitive.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IPrimitive.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) > ~_Self

**Inherited from:** IPrimitive.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IPrimitive.translated

Translated.

::
    
    def ungrouped(self) -> Tuple[IPrimitive, ...]

ungrouped self in recursion.

If there's a sub group in the content, the sub group will be ungrouped too.

Return a tuple of IPrimitive.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IPrimitive.v_mirrored

Vertical mirrored.

ILayer
++++++++

::
    
    class ILayer

Interface of Layer.

Subclasses
________________

::
    
    UnknownLayer, Layer

Class variables
________________

::
    
    var description: str
    var name: str
    var order: int
    var process: IProcess
    var purpose: IPurpose
    var value: Tuple[int, int]

ILayered
++++++++++++

::
    
    class ILayered

Subclasses
_____________

::
    
    IPrimitive

Class variables
__________________

::
    
    var layer: ILayer

ILibrary
++++++++++

::
    
    class ILibrary(*args, **kwds)

Super class of containers. An IRunnableContainer runs processors to process itself and its content.

Ancestors
__________

::
    
    IUpdatable, IRunnableContainer, typing.Generic, IRunnable

Subclasses
_____________

::
    
    Library

Class variables
_________________

::
    
    var content: Tuple[ICell, ...]

ILink
_______

::
    
    class ILink

Interface of CellRef

Ancestors
____________

::
    
    ICurveLike, ICurvedCellRef, ICurved, ICellRef, IUpdatable, IElement, 
    IRunnable, IAffineTransformable

Subclasses
____________

::
    
    ILinkBetween, LinkSmooth

Class variables
_________________

::
    
    var raw_curve: ICurve

Methods
_______

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurvedCellRef.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurvedCellRef.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ICurvedCellRef.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

ILinkBetween
++++++++++++++

::
    
    class ILinkBetween

Interface of CellRef.

Ancestors
___________

::
    
    ILink, ICurveLike, ICurvedCellRef, ICurved, ICellRef, 
    IUpdatable, IElement, IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    IMetalLineBetween, IWaveguideBetween

Class variables
_________________

::
    
    var raw_curve: ICurve

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self
    
**Inherited from:** ILink.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ILink.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ILink.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILink.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ILink.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ILink.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ILink.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self
    
**Inherited from:** ILink.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ILink.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ILink.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

ILinkType
++++++++++

::
    
    class ILinkType

Ancestors
____________

::
    
    IUpdatable

Subclasses
____________

::
    
    IMetalLineType, IWaveguideType

Methods
__________

::
    
    def port_width(self) -> float

ILinkingPolicy
++++++++++++++++

::
    
    class ILinkingPolicy

Subclasses
_____________

::
    
    LinkingPolicy

IMaterial
++++++++++

::
    
    class IMaterial

Subclasses
_____________

::
    
    IElectronicMaterial, IPhotonicMaterial

Class variables
__________________

::
    
    var name: str

IMetalLineBetween
++++++++++++++++++

::
    
    class IMetalLineBetween

Interface of CellRef.

Ancestors
___________

::
    
    ILinkBetween, ILink, ICurveLike, ICurvedCellRef, ICurved, ICellRef, IUpdatable, 
    IElement, IRunnable, IAffineTransformable

Subclasses
___________

::
    
    MetalLineBetween, fnpcell,_autolink.link_between.metal.MetalLineBetween

Class variables
________________

::
    
    var end: IPin
    var start: IPin

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILinkBetween.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ILinkBetween.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**8Inherited from:** ILinkBetween.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILinkBetween.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self
    
**Inherited from:** ILinkBetween.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ILinkBetween.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ILinkBetween.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_environment(self: ~_Self, flyline_layer: Optional[ILayer] = None, 
                            min_distance: Optional[float] = None, start_distance: Optional[float] = None, 
                            end_distance: Optional[float] = None, metal_line_type: Union[None, IMetalLineType, 
                            Iterable[Tuple[float, IMetalLineType]]] = None, 
                            fitting_function: Optional[Callable[[Tuple[Tuple[float, float], ...]], ICurve]] = None, 
                            auto_vias: Optional[IAutoVias] = None, **kwargs: Any) -> ~_Self

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ILinkBetween.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self
    
**Inherited from:** ILinkBetween.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ILinkBetween.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

IMetalLineLike
+++++++++++++++

::
    
    class IMetalLineLike

Interface of CellRef

Ancestors
___________

::
    
    ICurveLike, ICurvedCellRef, ICurved, ICellRef, IUpdatable, IElement, 
    IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    MetalLine, fnpcell_autolink.link_between.metal.MetalLineBetween

Class variables
_________________

::
    
    var raw_curve: ICurve

Instance variables
_____________________

::
    
    var curve_length: float

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurvedCellRef.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurvedCellRef.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ICurvedCellRef.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

IMetalLineType
++++++++++++++++

::
    
    class IMetalLineType

Ancestors
___________

::
    
    ILinkType, IUpdatable

Subclasses
___________

::
    
    MetalLineType

Class variables
__________________

::
    
    var metal_stack: IMetalStack
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]

Static methods
________________

::
    
    def is_class_isomorphic_to(other: Type[Any]) -> bool

Methods
__________

::
    
    def is_isomorphic_to(self, other: IMetalLineType) -> bool

IMetalStack
++++++++++++

::
    
    class IMetalStack

Ancestors
_____________

::
    
    IUpdatable

Subclasses
_____________

::
    
    MetalStack

Class variables
_____________________

::
    
    var connectivity: Mapping[ILayer, FrozenSet[ILayer]]
    var layers: Tuple[ILayer, ...]

Methods
__________

::
    
    def is_metal(self, layer: ILayer) -> bool

IOwned
++++++++

::
    
    class IOwned

Subclasses
_____________

::
    
    IOwnedTerminal

Class variables
__________________

::
    
    var owner: ICellRef

IOwnedPin
++++++++++++

::
    
    class IOwnedPin

Base class of pin and port.

Ancestors
____________

::
    
    IPin, IOwnedTerminal, IOwned, ITerminal, IUpdatable, IRa, IPositioned, IRunnable

Subclasses
_____________

::
    
    OwnedPin

Class variables
_________________

::
    
    var raw: IPin

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IPin.advanced

Return an IRay with advanced position through orientation.

::
    
    def c_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.c_mirrored

Owner center mirrored.

::
    
    def h_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.h_mirrored

Owner horizontal mirrored.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IPin.opposite

Return an IRay with same position but opposite orientation.

::
    
    def repositioned(self, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.repositioned

Positioned at new point,Owner will translated.

::
    
    def rotated(self, degrees: Optional[float] = None, radians: Optional[float] = None) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.rotated

Rotated both degrees and radians.

::
    
    def v_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.v_mirrored

Owner vertical mirrored.

IOwnedPort
+++++++++++

::
    
    class IOwnedPort

Interface of OwnedPort.

Ancestors
___________

::
    
    IPort, IOwnedTerminal, IOwned, ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Subclasses
____________

::
    
    OwnedPort

Class variables
_________________

::
    
    var raw: IPort

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IPort.advanced

Return an IRay with advanced position through orientation.

::
    
    def c_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.c_mirrored

Owner center mirrored.

::
    
    def h_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.h_mirrored

Owner horizontal mirrored.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IPort.opposite

Return an IRay with same position but opposite orientation.

::
    
    def repositioned(self, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.repositioned

Positioned at new point,Owner will translated.

::
    
    def rotated(self, degrees: Optional[float] = None, radians: Optional[float] = None) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.rotated

Rotated both degrees and radians.

::
    
    def v_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedTerminal.v_mirrored

Owner vertical mirrored.

IOwnedTerminal
+++++++++++++++++

::
    
    class IOwnedTerminal

Base class of pin and port.

Ancestors
__________

::
    
    IOwned, ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Subclasses
_____________

::
    
    IOwnedPin, IOwnedPort

Class variables
_________________

::
    
    var raw: ITerminal

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** ITerminal.advanced

Return an IRay with advanced position through orientation.

::
    
    def c_mirrored(self) -> IOwnedTerminal

Owner center mirrored.

::
    
    def flatten(self) -> ITerminal

::
    
    def h_mirrored(self) -> IOwnedTerminal

Owner horizontal mirrored.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** ITerminal.opposite

Return an IRay with same position but opposite orientation.

::
    
    def repositioned(self, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> IOwnedTerminal

Positioned at new point,Owner will translated.

::
    
    def rotated(self, degrees: Optional[float] = None, radians: Optional[float] = None) -> IOwnedTerminal

Rotated both degrees and radians.

::
    
    def v_mirrored(self) -> IOwnedTerminal

Owner vertical mirrored.

::
    
    def with_name(self: ~_Self, name: Union[None, str, Hidden]) -> ~_Self

IPhotonicMaterial
++++++++++++++++++++

::
    
    class IPhotonicMaterial

Ancestors
____________

::
    
    IMaterial

Class variables
__________________

::
    
    var refractive_index: float

IPin 
++++++

::
    
    class IPin

Base class of pin and port.

Ancestors
_____________

::
    
    ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Subclasses
_____________

::
    
    OwnedPin, Pin fnpcell.cell.pin._PinMixin, IOwnedPin

Class variables
_____________________

::
    
    var metal_line_type: IMetalLineType

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self
    
**Inherited from:** ITerminal.advanced

Return an IRay with advanced position through orientation.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** ITerminal.opposite

Return an IRay with same position but opposite orientation.

IPolygon
++++++++++

::
    
    class IPolygon

Interface of element,element is geometry with layer.

Ancestors
___________

::
    
    IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
____________

::
    
    Polygon, IPolyline

Class variables
__________________

::
    
    var raw_shape: IShape

Instance variables
______________________


::
    
    var polygon_points: Tuple[Tuple[float, float], ...]
    var shape

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IPrimitive.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IPrimitive.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IPrimitive.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IPrimitive.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IPrimitive.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IPrimitive.v_mirrored

Vertical mirrored.

IPolygonSet
++++++++++++++

::
    
    class IPolygonSet

Interface of element,element is geometry with layer.

Ancestors
____________

::
    
    IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
___________

::
    
    PolygonSet

Class variables
__________________

::
    
    var polygons: Tuple[IPolygon, ...]
    var region: IRegion

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:**  IPrimitive.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IPrimitive.h_mirrored

Horizontal mirrored.

::
    
    def inverted(self, bounding_shape: IShape) -> IPolygonSet

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                    origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IPrimitive.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def run(self, processor: IProcessor)

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IPrimitive.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IPrimitive.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IPrimitive.v_mirrored

Vertical mirrored.

IPolyline
+++++++++++

::
    
    class IPolyline

Interface of element,element is geometry with layer.

Ancestors
____________

::
    
    ICurved, ICurveLike, IPolygon, IPrimitive, 
    ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
____________

::
    
    Polyline

Class variables
________________

::
    
    var end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]]
    var extension: Tuple[float, float]
    var final_stroke_offset: float
    var final_stroke_width: float
    var miter_limit: float
    var stroke_offset: float
    var stroke_width: float
    var taper_function: ITaperCallable

Instance variables
____________________

::
    
    var curve_length: float
    var end_rays: Tuple[IRay, IRay]
    var polyline_points: Tuple[Tuple[float, float], ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurved.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurved.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurved.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurved.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurved.v_mirrored

Vertical mirrored.

IPort
++++++

::
    
    class IPort

Interface of Port.

Ancestors
_____________

::
    
    ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Subclasses
___________

::
    
    Port, fnpcell.cell.port._PortMixin, IOwnedPort

Class variables
__________________

::
    
    var waveguide_type: IWaveguideType

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** ITerminal.advanced

Return an IRay with advanced position through orientation.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** ITerminal.opposite

Return an IRay with same position but opposite orientation.

IPositioned
+++++++++++++

::
    
    class IPositioned

IPositioned has a position of (x, y).

Subclasses
___________

::
    
    IRay, SampleInfo

Class variables
__________________

::
    
    var position: Tuple[float, float]

Instance variables
____________________

::
    
    var x: float
    var y: float

IPrimitive
++++++++++++

::
    
    class IPrimitive

Interface of element,element is geometry with layer.

Ancestors
___________

::
    
    ILayered, IElement, IRunnable, IAffineTransformable

Subclasses
_____________

::
    
    Text, IGroup, IPolygon, IPolygonSet

Class variables
_________________

::
    
    var layer: ILayer

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IElement.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IElement.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IElement.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IElement.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IElement.v_mirrored

Vertical mirrored.

::
    
    def with_layer(self: ~_Self, layer: ILayer) -> ~_Self

IProcess
+++++++++

::
    
    class IProcess

Subclasses
_____________

::
    
    UnknownProcess, Process

Class variables
__________________

::
    
    var description: str
    var name: str
    var order: int
    var value: int

IProcessor
++++++++++++

::
    
    class IProcessor

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Subclasses
____________

::
    
    fnpcell.gdsii.gds_importer._ReferenceCounter, GDSWriter, fnpcell.gdsii.gds_writer._CellCollector, 
    LayoutWriter, NetlistWriter, fnpcell.internal.plogic_util._LayoutCellCollector, 
    fnpcell.internal.plogic_util._NetlistCellCollector, fnpcell.internal.util.layout_util._BBox, 
    Statistics, SPCWriter, fnpcell.netlist.spc_writer._CellCollector, MatplotlibShower, PortOwnerChecker

Methods
__________

::
    
    def enter(self, target: Any) -> bool

Called before processing a target. Return True to continue processing child content. 
False to stop here and run exit for the target

::
    
    def exit(self, target: Any) -> None

Called after processing a target.

IPurpose
++++++++++

::
    
    class IPurpose

Subclasses
____________

::
    
    UnknownPurpose, Purpose

Class variables
__________________

::
    
    var description: str
    var name: str
    var order: int
    var value: int

IRay
+++++

::
    
    class IRay

IRay has a position and an orientation.

Ancestors
__________

::
    
    IPositioned

Subclasses
____________

::
    
    ITerminal, Ray

Class variables
________________

::
    
    var orientation: float

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self
    
Return an IRay with advanced position through orientation.

::
    
    def opposite(self: ~_Self) -> ~_Self

Return an IRay with same position but opposite orientation.

IRegion
++++++++

::
    
    class IRegion

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
____________

::
    
    IAffineTransformable

Subclasses
____________

::
    
    Region

Class variables
__________________

::
    
    var shapes: Tuple[IShape, ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.h_mirrored

Horizontal mirrored.

::
    
    def merged(self) -> IRegion

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** IAffineTransformable.rotated

Return a new cell reference rotated, either degrees or radians must be provided. ]
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.

IRunnable
+++++++++++

::
    
    class IRunnable

Super class of all element. An IRunnable runs processors to process itself.

Subclasses
_____________

::
    
    IElement, IRunnableContainer, ITerminal

Methods
__________

::
    
    def run(self: ~_Self, processor: IProcessor) -> ~_Self

IRunnableContainer
++++++++++++++++++++

::
    
    class IRunnableContainer(*args, **kwds)

Super class of containers. An IRunnableContainer runs processors to process itself and its content.

Ancestors
____________

::
    
    typing.Generic, IRunnable

Subclasses
____________

::
    
    ICell, IComposite, IGroup, ILibrary

Class variables
_________________

::
    
    var content: Iterable[~_Ru]

Methods
__________

::
    
    def run(self: ~_Self, processor: IProcessor) -> ~_Self

IShape
++++++++++

::
    
    class IShape

IAffineTransformable supports transform, can be scaled, rotated, translated, h_mirrored, v_mirrored, c_mirrored.

Ancestors
____________

::
    
    IAffineTransformable

Subclasses
_____________

::
    
    Shape

Class variables
__________________

::
    
    var transform: Affine2D

Instance variables
_____________________

::
    
    var shape_points: Tuple[Tuple[float, float], ...]

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** IAffineTransformable.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self
    
**Inherited from:** IAffineTransformable.h_mirrored

Horizontal mirrored.

::
    
    def offsetted(self, offset: float) -> IShape

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
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** IAffineTransformable.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** IAffineTransformable.v_mirrored

Vertical mirrored.

IStraightWaveguideFactory
+++++++++++++++++++++++++++

::
    
    class IStraightWaveguideFactory(*args, **kwargs)

Base class for protocol classes.

Protocol classes are defined as::
    
    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize 
structural subtyping (static duck-typing), for example::

    class C:
        def meth(self) -> int:
            return 0

        def func(x: Proto) -> int:
            return x.meth()

        func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with @typing.runtime_checkable act 
as simple-minded runtime protocols that check only the presence of given attributes, 
ignoring their type signatures. Protocol classes can be generic, they are defined as::
    
    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...

Ancestors
__________

::
    
    typing.Protocol, typing.Generic

ITaperCallable
+++++++++++++++++

::
    
    class ITaperCallable

Subclasses
_____________

::
    
    TaperFunctionLinear, TaperFunctionParabolic

ITerminal
+++++++++++

::
    
    class ITerminal

Base class of pin and port.

Ancestors
___________

::
    
    IUpdatable, IRay, IPositioned, IRunnable

Subclasses
_____________

::
    
    IOwnedTerminal, IPin, IPort

Class variables
_________________\

::
    
    var hidden: bool
    var name: Optional[str]
    var orientation: float
    var shape: IShape

Instance variables
_____________________

    var annotation: IComposite
    var disabled: bool

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IRay.advanced

Return an IRay with advanced position through orientation.

::
    
    def matches(self, other: ITerminal) -> bool

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IRay.opposite

Return an IRay with same position but opposite orientation.

::
    
    def run(self, processor: IProcessor)

::
    
    def with_name(self: ~_Self, name: Union[None, str, Hidden]) -> ~_Self

::
    
    def with_orientation(self: ~_Self, *, degrees: Optional[float] = None, 
                            radians: Optional[float] = None) -> ~_Self

IUpdatable
++++++++++++

::
    
    class IUpdatable

Subclasses
_____________

::
    
    ICell, ICellRef, ILibrary, ILinkType, IMetalStack, ITerminal, TransformMixin

Methods
__________

::
    
    def updated(self: ~_Self, **kwargs: Any) -> ~_Self

IViasFactory
++++++++++++++++

::
    
    class IViasFactory(*args, **kwargs)

Base class for protocol classes.

Protocol classes are defined as::
    
    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize structural 
subtyping (static duck-typing), for example::
    
    class C:
        def meth(self) -> int:
            return 0

        def func(x: Proto) -> int:
            return x.meth()

        func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with @typing.runtime_checkable act 
as simple-minded runtime protocols that check only the presence of given attributes, 
ignoring their type signatures. Protocol classes can be generic, they are defined as::
    
    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...

Ancestors
__________

::
    
    typing.Protocol, typing.Generic

IWaveguideBetween
++++++++++++++++++

::
    
    class IWaveguideBetween

Interface of CellRef.

Ancestors
____________

::
    
    ILinkBetween, ILink, ICurveLike, ICurvedCellRef, ICurved, 
    ICellRef, IUpdatable, IElement, IRunnable, IAffineTransformable

Subclasses
____________

::
    
    WaveguideBetween, fnpcell_autolink.link_between.wg.WaveguideBetween

Class variables
________________

::
    
    var end: IPort
    var start: IPort

Methods
____________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILinkBetween.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ILinkBetween.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ILinkBetween.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ILinkBetween.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ILinkBetween.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ILinkBetween.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ILinkBetween.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_environment(self: ~_Self, flyline_layer: Optional[ILayer] = None, 
                            linking_policy: Optional[ILinkingPolicy] = None, 
                            link_type: Optional[IWaveguideType] = None, 
                            straight_factory: Optional[IStraightWaveguideFactory] = None, 
                            bend_factory: Optional[IBendWaveguideFactory] = None, 
                            **kwargs: Any) -> ~_Self

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ILinkBetween.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ILinkBetween.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ILinkBetween.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

IWaveguideLike
+++++++++++++++

::
    
    class IWaveguideLike

Interface of CellRef.

Ancestors
__________

::
    
    ICurveLike, ICurvedCellRef, ICurved, ICellRef, IUpdatable, 
    IElement, IRunnable, IAffineTransformable

Subclasses
___________

::
    
    Waveguide, LinkSmooth, fnpcell_autolink.link_between.wg.WaveguideBetween

Class variables
__________________

::
    
    var raw_curve: ICurve

Instance variables
_____________________

::
    
    var curve_length: float

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.c_mirrored

Center mirrored.

::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.h_mirrored

Horizontal mirrored.

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self

**Inherited from:** ICurvedCellRef.rotated

Return a new cell reference rotated, either degrees or radians must be provided. 
If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** ICurvedCellRef.scaled

scaled at center.

::
    
    def translated(self: ~_Self, tx: float, ty: float) -> ~_Self

**Inherited from:** ICurvedCellRef.translated

Translated.

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** ICurvedCellRef.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self

**Inherited from:** ICurvedCellRef.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self

**Inherited from:** ICurvedCellRef.with_ports

If a class derived from ICellRef does not implement this method, it cannot be instantiated. 
If a derived class of ICellRef implements this method, …

IWaveguideType
++++++++++++++++

::
    
    class IWaveguideType

Ancestors
___________

::
    
    ILinkType, IUpdatable

Subclasses
_____________

::
    
    WaveguideType

Class variables
__________________

::
    
    var bend_factory: IBendWaveguideFactory
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]
    var straight_factory: IStraightWaveguideFactory

Static methods
________________

::
    
    def is_class_isomorphic_to(other: Type[Any]) -> bool

Instance variables
_____________________

::
    
    var band: IBand

Methods
__________

::
    
    def is_isomorphic_to(self, other: IWaveguideType) -> bool

Offset
++++++++

::
    
    class Offset(x: Union[None, float, Absolute] = None, y: Union[None, float, Absolute] = None, 
                    relative_to: RelativeTo = RelativeTo.PREV)

Offset(x: Union[NoneType, float, fnpcell.interfaces.Absolute] = None, 
y: Union[NoneType, float, fnpcell.interfaces.Absolute] = None, 
relative_to: fnpcell.interfaces.RelativeTo = fnpcell.interfaces.RelativeTo.PREV)

Class variables
__________________

::
    
    var relative_to: RelativeTo
    var x: Union[None, float, Absolute]
    var y: Union[None, float, Absolute]

Static methods
_________________

::
    
    def from_end(x: float, y: float)

::
    
    ef from_start(x: float, y: float)

::
    
    def until_x(x: float)

::
    
    def until_y(y: float)

Ray
+++++

::
    
    class Ray(position: Tuple[float, float], orientation: float)

Ray(position: Tuple[float, float], orientation: float)

Ancestors
_____________

::
    
    IRay, IPositioned

Class variables
__________________

::
    
    var orientation: float
    var position: Tuple[float, float]

Methods
_______

::
    
    def advanced(self, distance: float) -> IRay

**Inherited from:** IRay.advanced

Return an IRay with advanced position through orientation.

::
    
    def opposite(self) -> IRay

**Inherited from:** IRay.opposite

Return an IRay with same position but opposite orientation.

RelativeTo
++++++++++++

::
    
    class RelativeTo(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.Enum

Class variables
_________________

::
    
    var END
    var PREV
    var START

SampleInfo
++++++++++++

::
    
    class SampleInfo(position: Tuple[float, float], orientation: float, length: float)

SampleInfo(position: Tuple[float, float], orientation: float, length: float)

Ancestors
__________

::
    
    IPositioned

Class variables
________________

::
    
    var length: float
    var orientation: float
    var position: Tuple[float, float]

TaperFunction
++++++++++++++++

::
    
    class TaperFunction

Class variables
__________________

::
    
    var LINEAR: ITaperCallable
    var PARABOLIC: ITaperCallable

TaperFunctionLinear
++++++++++++++++++++

::
    
    class TaperFunctionLinear

TaperFunctionLinear()

Ancestors
_____________

::
    
    ITaperCallable

TaperFunctionParabolic
+++++++++++++++++++++++++

::
    
    class TaperFunctionParabolic

TaperFunctionParabolic()

Ancestors
___________

::
    
    ITaperCallable

TextBaseline
++++++++++++++

::
    
    class TextBaseline(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.Enum

Class variables
__________________

::
    
    var ALPHABETIC
    var BOTTOM
    var TOP

Type2TypeMeta
++++++++++++++++

::
    
    class Type2TypeMeta(*args, **kwargs)

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC. An ABC can be subclassed directly, and then 
acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) 
and unrelated ABCs as 'virtual subclasses' – these and their descendants will be considered 
subclasses of the registering ABC by the built-in issubclass() function, but the registering 
ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by 
the registering ABC be callable (not even via super()).

Ancestors
_____________

::
    
    abc.ABCMeta, builtins.type

Subclasses
_____________

::
    
    MetalLineTypeMeta, WaveguideTypeMeta

Unimplemented
++++++++++++++++++

::
    
    class Unimplemented(message: str)

Unimplemented(message: str)

Class variables
_________________

::
    
    var message: str

UnknownLayer
+++++++++++++

::
    
    class UnknownLayer(value: Tuple[int, int], description: str = '', order: int = -1, 
                        name_template: str = 'Layer({value[0]}/{value[1]})')

UnknownLayer(value: Tuple[int, int], description: str = '', order: int = -1, name_template: 
str = 'Layer({value[0]}/{value[1]})')

Ancestors
____________

::
    
    ILayer

Class variables
__________________

::
    
    var description: str
    var name_template: str
    var order: int
    var value: Tuple[int, int]

Instance variables
_____________________

::
    
    var name: str
    var process: IProcess
    var purpose: IPurpose

UnknownProcess
+++++++++++++++++

::
    
    class UnknownProcess(value: int, description: str = '', order: int = -1, 
                            name_template: str = 'Process(value)')

UnknownProcess(value: int, description: str = '', order: int = -1, name_template: str = 'Process(value)')

Ancestors
__________

::
    
    IProcess

Class variables
__________________

::
    
    var description: str
    var name_template: str
    var order: int
    var value: int

Instance variables
____________________

::
    
    var name: str

UnknownPurpose
++++++++++++++++

::
    
    class UnknownPurpose(value: int, description: str = '', order: int = -1, name_template: str = 'Purpose(value)')

UnknownPurpose(value: int, description: str = '', order: int = -1, name_template: str = 'Purpose(value)')

Ancestors
____________

::
    
    IPurpose

Class variables
____________________

::
    
    var description: str
    var name_template: str
    var order: int
    var value: int

Instance variables
____________________

::
    
    var name: str

::
    
    class VertialAlign(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
____________

::
    
    enum.Enum

Class variables
_________________

::
    
    var BOTTOM
    var MIDDLE
    var TOP

Waypoints
+++++++++++

::
    
    class Waypoints(start: +_L, middle: Tuple[IRay, ...], end: +_R)

Waypoints(args, \*kwds)

Ancestors
____________

::
    
    typing.Generic

Class variables
__________________

::
    
    var end: +_R
    var middle: Tuple[IRay, ...]
    var start: +_L