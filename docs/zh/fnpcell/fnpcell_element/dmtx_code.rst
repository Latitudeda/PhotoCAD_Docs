Module fnpcell.element.dmtx_code
===================================

Functions
----------

::
    
    def encode_text_mode(msg: str, codepage: Dict[str, bytes], magic: bytes, multiset: bool)

Encode to datamatrix text modes (C40, TEXT, X12).

::
    
    def encode_to_C40(msg: str)

::
    
    def encode_to_X12(msg: str)

::
    
    def encode_to_ascii(msg: str)

::
    
    def encode_to_edifact(msg: str)

::
    
    def encode_to_text(msg: str)

Encode to datamatrix.text.

::
    
    def pack(ascii: bytes, tail: bytes = b'')

::
    
    def pack_words(raw: bytes)

3 raw bytes to 2 encoded bytes stuffing for datamatrix text modes.

::
    
    def tokenize(enc: bytes)

Classes
---------

::
    
    class DataMatrixCode(data: str, layer: ILayer, invert: bool = False, pixel_size: float = 5,
                         transform: Affine2D = Affine2D.identity())
    
    DataMatrixCode(args: Any, *kwargs: Any)

Ancestors
+++++++++++

::
    
    TransformMixin, IUpdatable, IGroup, IRunnableContainer, typing.Generic, IPrimitive, 
    ILayered, IElement, IRunnable, IAffineTransformable

Class variables
+++++++++++++++++

::
    
    var data: str
    var invert: bool
    var layer: ILayer
    var pixel_size: float
    var transform: Affine2D

Static methods
++++++++++++++++

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
++++++++++++++++++++

::
    
    var content : Tuple[IPrimitive, ...]

Methods
++++++++

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

Return a new cell reference rotated, either degrees or radians must be provided. If both provided, radians is used …

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

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

::
    
    class DataMatrixCodeModel(data: str, rect: bool = False)

Create a datamatrix code for message 'msg'. Set rect=True for a rectangular datamatrix (if possible). 
Default is False, resulting in a square datamatrix.

Class variables
++++++++++++++++

::
    
    var m: Dict[int, Dict[int, bool]]

Instance variables
++++++++++++++++++++

::
    
    var colrow