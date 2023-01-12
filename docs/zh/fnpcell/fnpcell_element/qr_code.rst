Module fnpcell.element.qr_code
===============================

Classes
---------

ErrorCorrection
+++++++++++++++++

::
    
    class ErrorCorrection(i: int, fb: int)

An enumeration.

Ancestors
____________

::
    
    enum.Enum

Class variables
__________________

::
    
    var HIGH
    var LOW
    var MEDIUM
    var QUARTILE
    var formatbits: int
    var ordinal: int

::
    
    class QRCode(data: str, layer: ILayer, invert: bool = False, pixel_size: float = 5, 
                    error_correction: ErrorCorrection = ErrorCorrection.HIGH, 
                    transform: Affine2D = Affine2D.identity())

QRCode(args: Any, \*kwargs: Any)

Ancestors
_____________

::
    
    TransformMixin, IUpdatable, IGroup, IRunnableContainer, typing.Generic, 
    IPrimitive, ILayered, IElement, IRunnable, IAffineTransformable

Class variables
__________________

::
    
    var data: str
    var error_correction: ErrorCorrection
    var invert: bool
    var layer: ILayer
    var pixel_size: float
    var transform: Affine2D

Static methods
_________________

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None, 
                            transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, the …

::
    
    ef transform_from_origin(origin: Optional[Tuple[float, float]] = None, 
                                transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_origin

Returns an Affine2D that is the result of the matrix product of the given transformation and 
the translation transformation at the given origin, It …

Instance variables
_____________________

::
    
    var content: Tuple[IPrimitive, ...]

Methods
________

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

QRCodeModel
++++++++++++++

::
    
    class QRCodeModel(version: int, errcorlvl: ErrorCorrection, 
                        datacodewords: Union[bytes, Sequence[int]], msk: int)

A QR Code symbol, which is a type of two-dimension barcode. Invented by Denso Wave and 
described in the ISO/IEC 18004 standard. Instances of this class represent an immutable 
square grid of dark and light cells. The class provides static factory functions to create 
a QR Code from text or binary data. The class covers the QR Code Model 2 specification, 
supporting all versions (sizes) from 1 to 40, all 4 error correction levels, 
and 4 character encoding modes.

Ways to create a QR Code object: - High level: Take the payload data and call QRCode.encode_text() 
or QRCode.encode_binary(). - Mid level: Custom-make the list of segments and call 
QRCode.encode_segments(). - Low level: Custom-make the array of data 
codeword bytes (including segment headers and final padding, excluding error correction codewords), 
supply the appropriate version number, and call the QRCode() constructor. 
(Note that all ways require supplying the desired error correction level.)

Creates a new QR Code with the given version number, error correction level, 
data codeword bytes, and mask number. This is a low-level API that most users 
should not use directly. A mid-level API is the encode_segments() function.

Class variables
__________________

::
    
    var MAX_VERSION: int
    var MIN_VERSION: int

Static methods
________________

::
    
    def encode_binary(data: Union[bytes, Sequence[int]], ecl: ErrorCorrection) -> QRCodeModel

Returns a QR Code representing the given binary data at the given error correction level. 
This function always encodes using the binary segment mode, not any text mode. 
The maximum number of bytes allowed is 2953. The smallest possible QR Code version 
is automatically chosen for the output. The ECC level of the result may be higher 
than the ecl argument if it can be done without increasing the version.

::
    
    def encode_segments(segs: Sequence[ForwardRef('Segment')], ecl: ErrorCorrection, minversion: int = 1, 
                        maxversion: int = 40, mask: int = -1, boostecl: bool = True) -> QRCodeModel

Returns a QR Code representing the given segments with the given encoding parameters. 
The smallest possible QR Code version within the given range is automatically chosen 
for the output. Iff boostecl is true, then the ECC level of the result may be higher 
than the ecl argument if it can be done without increasing the version. 
The mask number is either between 0 to 7 (inclusive) to force that mask, 
or -1 to automatically choose an appropriate mask (which may be slow). 
This function allows the user to create a custom sequence of segments that 
switches between modes (such as alphanumeric and byte) to encode text in less space. 
This is a mid-level API; the high-level API is encode_text() and encode_binary().

::
    
    def encode_text(text: str, ecl: ErrorCorrection) -> QRCodeModel

Returns a QR Code representing the given Unicode text string at the given error correction level. 
As a conservative upper bound, this function is guaranteed to succeed for strings that have 738 
or fewer Unicode code points (not UTF-16 code units) if the low error correction level is used. 
The smallest possible QR Code version is automatically chosen for the output. The ECC level 
of the result may be higher than the ecl argument if it can be done without increasing the version.

Methods
________

::
    
    def get_error_correction_level(self) -> ErrorCorrection

Returns this QR Code's error correction level.

::
    
    def get_mask(self) -> int

Returns this QR Code's mask, in the range [0, 7].

::
    
    def get_module(self, x: int, y: int) -> bool

Returns the color of the module (pixel) at the given coordinates, which is False for light or True for dark. 
The top left corner has the coordinates (x=0, y=0). If the given coordinates are out of bounds, 
then False (light) is returned.

::
    
    def get_size(self) -> int

Returns this QR Code's size, in the range [21, 177].

::
    
    def get_version(self) -> int

Returns this QR Code's version number, in the range [1, 40].

Segment
+++++++++

::
    
    class Segment(mode: SegmentMode, numch: int, bitdata: Sequence[int])
    
A segment of character/binary/control data in a QR Code symbol. Instances of this class are immutable. 
The mid-level way to create a segment is to take the payload data and call a static factory function 
such as QrSegment.make_numeric(). The low-level way to create a segment is to custom-make the bit buffer 
and call the QrSegment() constructor with appropriate values. This segment class imposes no length restrictions, 
but QR Codes have restrictions. Even in the most favorable conditions, a QR Code can only hold 7089 characters of data. 
Any segment longer than this is meaningless for the purpose of generating QR Codes.

Creates a new QR Code segment with the given attributes and data. 
The character count (numch) must agree with the mode and the bit buffer length, 
but the constraint isn't checked. The given bit buffer is cloned and stored.

Static methods
_________________

::
    
    def get_total_bits(segs: Sequence[ForwardRef('Segment')], version: int) -> Optional[int]

Calculates the number of bits needed to encode the given segments at the given version. 
Returns a non-negative number if successful. Otherwise returns None if a segment has too 
many characters to fit its length field.

::
    
    def is_alphanumeric(text: str) -> bool

::
    
    def is_numeric(text: str) -> bool

::
    
    def make_alphanumeric(text: str) -> Segment

Returns a segment representing the given text string encoded in alphanumeric mode. 
The characters allowed are: 0 to 9, A to Z (uppercase only), space, dollar, percent, 
asterisk, plus, hyphen, period, slash, colon.

::
    
    def make_bytes(data: Union[bytes, Sequence[int]]) -> Segment
    
Returns a segment representing the given binary data encoded in byte mode. 
All input byte lists are acceptable. Any text string can be converted to UTF-8 bytes (s.encode("UTF-8")) 
and encoded as a byte mode segment.

::
    
    def make_eci(assignval: int) -> Segment

Returns a segment representing an Extended Channel Interpretation (ECI) designator with the given assignment value.

::
    
    def make_numeric(digits: str) -> Segment

Returns a segment representing the given string of decimal digits encoded in numeric mode.

::
    
    def make_segments(text: str) -> List[Segment]
    
Returns a new mutable list of zero or more segments to represent the given Unicode text string. 
The result may use various segment modes and switch modes to optimize the length of the bit stream.

Methods
____________

::
    
    def get_data(self, copy: bool = True) -> List[int]

Returns a new copy of the data bits of this segment.

::
    
    def get_mode(self) -> SegmentMode

Returns the mode field of this segment.

::
    
    def get_num_chars(self) -> int

Returns the character count field of this segment.

SegmentMode
+++++++++++++

::
    
    class SegmentMode(modebits: int, charcounts: Tuple[int, int, int])

Describes how a segment's data bits are interpreted. Immutable.

Ancestors
___________

::
    
    enum.Enum

Class variables
________________

::
    
    var ALPHANUMERIC
    var BYTE
    var ECI
    var KANJI
    var NUMERIC

Methods
________

::
    
    def get_mode_bits(self) -> int

Returns an unsigned 4-bit integer value (range 0 to 15) representing the mode indicator bits for this mode object.

::
    
    def num_char_count_bits(self, ver: int) -> int

Returns the bit width of the character count field for a segment in this mode in a QR Code at the given version number. 
The result is in the range [0, 16].