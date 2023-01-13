Module fnpcell.element.group
==============================

Functions
-----------

::
    
    def new_group(*primitives: IPrimitive, origin: Optional[Tuple[float, float]] = None,
                     transform: Affine2D = Affine2D.identity()) -> Group

Create a group.
This is a container of primitives(eg. primitive is a polygon with layer.).

Classes
----------

::
    
    class Group(content: Tuple[IPrimitive, ...], transform: Affine2D)

Group is a dataclass for defining a Group.

Ancestors
+++++++++++

::
    
    TransformMixin, IUpdatable, IGroup, IRunnableContainer, typing.Generic, 
    IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Class variables
+++++++++++++++++

::
    
    var content: Tuple[IPrimitive, ...]
    var transform: Affine2D

Static methods
+++++++++++++++++

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
+++++++++++++++++++

::
    
    var layer: ILayer

Return layer.

Methods
++++++++

::
    
    def appended(self, *nodes: IPrimitive) -> IGroup

Add content.

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

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
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *,
                 center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.scaled

scaled at center.

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
    
    def ungrouped(self) -> Tuple[IPrimitive, ...]

**Inherited from:** IGroup.ungrouped

ungrouped self in recursion …

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** TransformMixin.v_mirrored

Vertical mirrored.

::
    
    def with_layer(self, layer: ILayer)