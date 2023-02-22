Module fnpcell.gdsii.gds_io
=============================

Functions
------------

normalize_angle
++++++++++++++++

::
    
    def normalize_angle(angle: float)

Normalize angle into [0, 360].

round_to_db_unit
++++++++++++++++++

::
    
    def round_to_db_unit(unit_ratio: float, value: float) -> int

str_to_bytes
++++++++++++++

::
    
    def str_to_bytes(string: str) -> bytes

unpack_int16s
+++++++++++++++

::
    
    def unpack_int16s(buf: bytes)

unpack_int32s
++++++++++++++++++

::
    
    def unpack_int32s(buf: bytes)

unpack_real8
++++++++++++++

::
    
    def unpack_real8(byte8: bytes) -> float

unpack_real8s
++++++++++++++++

::
    
    def unpack_real8s(buf: bytes)

unpack_uint16s
++++++++++++++++++

::
    
    def unpack_uint16s(buf: bytes)

Classes
--------

GDSInputParser
++++++++++++++++

::
    
    class GDSInputParser(input: io.IOBase)

Methods
_________

::
    
    def close(self)

::
    
    def opt_aref(self)

::
    
    def opt_attrtable(self)

::
    
    def opt_bgnstr(self)

::
    
    def opt_boundary(self)

::
    
    def opt_box(self)

::
    
    def opt_element(self)

::
    
    def opt_fonts(self)

::
    
    def opt_format_type(self)

::
    
    def opt_generations(self)

::
    
    def opt_libdirsize(self)

::
    
    def opt_libsecur(self)

::
    
    def opt_node(self)

::
    
    def opt_path(self)

::
    
    def opt_property(self)

::
    
    def opt_record(self, record_type: GDSRecordType)

::
    
    def opt_reflibs(self)

::
    
    def opt_sref(self)

::
    
    def opt_srfname(self)

::
    
    def opt_strans(self)


::
    
    def opt_strclass(self)

::
    
    def opt_structure(self)

::
    
    def opt_text(self)

::
    
    def parse_bgnlib(self)

::
    
    def parse_endel(self)

::
    
    def parse_endlib(self)

::
    
    def parse_endstr(self)

::
    
    def parse_header(self)

::
    
    def parse_libname(self)

::
    
    def parse_record(self, record_type: GDSRecordType)

::
    
    def parse_stream(self) -> Dict[str, Any]

::
    
    def parse_strname(self)

::
    
    def parse_textbody(self)

::
    
    def parse_units(self)

::
    
    def peek_next(self)

::
    
    def peek_record(self, record_type: GDSRecordType) -> bool

::
    
    def raw_next_record(self)

::
    
    def read_next(self)

::
    
    def rep0(self, parse: Callable[[], Optional[Any]])

::
    
    def rep0_element(self)

::
    
    def rep0_property(self)

::
    
    def rep0_record(self, record_type: GDSRecordType)

::
    
    def rep0_structure(self)

::
    
    def rep1(self, parse: Callable[[], Optional[Any]])

::
    
    def rep1_mask(self)

::
    
    def rep1_record(self, record_type: GDSRecordType)

GDSOutputWriter
+++++++++++++++++++

::
    
    class GDSOutputWriter(*, output: io.IOBase, lib_name: str = 'library', unit_ratio: float)

Methods
________

::
    
    def close(self)

::
    
    def write_angle(self, angle: float)

Marks in an angular rotation factor, measured in degrees and in counterclockwise direction. 
For an AREF, the ANGLE rotates the entire array lattice (with the individual array elements 
rigidly attached) about the array reference point. The default is 0.

::
    
    def write_annotation(self, *, layer: int, xy: Tuple[float, float], text: str, 
                            texttype: int = 0, transform: GDSTransform = GDSTransform(reflection=False, 
                            magnification=1, rotation=0))

::
    
    def write_aref(self)

Marks the beginning of an AREF (array reference) element.

::
    
    def write_bgnlib(self, local_datetime: Optional[datetime.datetime] = None)

::
    
    def write_bgnstr(self, local_datetime: Optional[datetime.datetime] = None)

::
    
    def write_boundary(self)

Marks the beginning of a boundary element.

::
    
    def write_bytes(self, buf: bytes)

::
    
    def write_colrow(self, col: int, row: int)

Marks the number of rows and columns in an array. Contains 4 bytes. The first 2 bytes contain the number of columns in the array. The third and fourth bytes contain the number of rows. Neither the number of columns nor the number of rows may exceed 32,767 (decimal), and both are positive.

::
    
    def write_datatype(self, datatype: int)

Marks the specify datatype. The value of the datatype must be in the range of a to 63.

::
    
    def write_datetime(self, local_datetime: Optional[datetime.datetime] = None)

::
    
    def write_endel(self)

Marks the end of an element.

::
    
    def write_endlib(self)

Marks the end of a library.

::
    
    def write_endstr(self)

Marks the end of a structure.

::
    
    def write_header(self)

::
    
    def write_int16(self, value: int)

::
    
    def write_int32(self, value: int)

::
    
    def write_layer(self, layer: int)

Marks the specified layer. The value of the layer should be in the range of a to 63.

::
    
    def write_libname(self, name: str)

Marks the name of the library. The library name must adhere to CDOS file name conventions 
for length and valid characters. The library name may include the file extension (.DB in most cases).

::
    
    def write_mag(self, magnification: float)

Marks a magnification factor, the default is 1.

::
    
    def write_nodata(self, value: int)

Marks record types for which no data exists.

::
    
    def write_path(self)

Marks the beginning of a path element.

::
    def write_pathtype(self, pathtype: int)

Marks a path type, the value of this record is 0 for square-ended paths that end 
flush with the endpoint, 1 for round-ended paths and 2 for square-ended paths that 
extend beyond half the width of the endpoint. path type 4 (CustomPlus products only) 
indicates a path with a variable square-ended extension. The default path type is 0.

::
    
    def write_polygon(self, *, xy: Iterable[Tuple[float, float]], layer: int, datatype: int = 0)

::
    
    def write_polyline(self, *, xy: Iterable[Tuple[float, float]], width: float, layer: int, 
                        close: bool = False, datatype: int = 0, pathtype: int = 0)

::
    
    def write_real64(self, value: float)

::
    
    def write_sname(self, name: str)

::
    
    def write_sref(self)

Marks the beginning of an SREF (structure reference) element.

::
    
    def write_strans(self, bits: int)

Marks an array of bits. Contains two bytes of bit flags for SREF, AREF, and text transformation. 
Bit 0 (the leftmost bit) specifies reflection. If it is set, then reflection about the X-axis is 
applied before angular rotation. For AREFs, the entire array lattice is reflected, with the 
individual array elements rigidly attached. Bit 13 flags absolute magnification. Bit 14 flags 
absolute angle. Bit 15 (the rightmost bit) and all remaining bits are reserved for future use 
and must be cleared. If this record is omitted, then the element is assumed to have no reflection 
and its magnification and angle are assumed to be non-absolute.

::
    
    def write_string(self, string: str)

Marks a character string for text presentation, up to 512 characters long.

::
    
    def write_strname(self, name: str)

Marks the structure name. A structure name may be up to 32 characters long. 
Legal structure name characters are: A through Z, a through z, 0 through 9, Underscore (_), 
Question mark (?), Dollar sign ($).

::
    
    def write_text(self)

Marks the beginning of a text element.

::
    
    def write_texttype(self, texttype: int)

Marks a text type, the value of the texttype must be in the range 0 to 63.

::
    
    def write_transform(self, transform: GDSTransform)

::
    
    def write_uint16(self, value: int)

::
    
    def write_uint8(self, value: int)

::
    
    def write_units(self, unit_ratio: float, db_unit: float)

Marks the size of the database unit. Contains 2 8-byte real numbers. 
The first is the size of a database unit in user units. The second is the size of 
a database unit in meters. For example, if your library was created with the default units 
(user unit = 1 micron and 1000 database units per user unit), then the first number would be .001 
and the second number would be 1E-9. Typically, the first number is less than 1, since you use 
more than 1 database unit per user unit. To calculate the size of a user unit in meters, divide 
the second number by the first.

::
    
    def write_width(self, width: float)

Marks the width of a specify path or text lines in data base units. A negative value for width means 
that the width is absolute, i.e., it is not affected by the magnification factor of any parent reference. 
The default is 1

::
    
    def write_xy(self, xy: Iterable[Tuple[float, float]], *, close: bool = False, min_length: int = 1)

Marks an array of XY coordinates in database units. Each X or Y coordinate is four bytes long. 
Path and boundary elements may have up to 200 pairs of coordinates. A path must have at least 2, 
and a boundary at least 4 pairs of coordinates. The first and last point of a boundary must coincide. 
A text or SREF element must have only one pair of coordinates. An AREF has exactly three pairs of 
coordinates, which specify the orthogonal array lattice. In an AREF the first point is the array 
reference point. The second point locates a position which is displaced from the reference point by 
the inter-column spacing times the number of columns. The third point locates a position which is 
displaced from the reference point by the inter-row spacing times the number of rows. A node may 
have from 1 to 50 pairs of coordinates. A box must have five pairs of coordinates with the first 
and last points coinciding.

GDSRecordDataType
++++++++++++++++++++

::
    
    class GDSRecordDataType(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.IntEnum, builtins.int, enum.Enum

Class variables
_________________

::
    
    var ASCII
    var BITARRAY
    var INT16
    var INT32
    var NODATA
    var REAL4
    var REAL8

GDSRecordType
+++++++++++++++

::
    
    class GDSRecordType(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.IntEnum. builtins.int. enum.Enum

Class variables
__________________

::
    
    var ANGLE
    var AREF
    var ATTRTABLE
    var BGNEXTN
    var BGNLIB
    var BGNSTR
    var BORDER
    var BOUNDARY
    var BOX
    var BOXTYPE
    var COLROW
    var CONTACT
    var DATATYPE
    var ELFLAGS
    var ELKEY
    var ENDEL
    var ENDEXTN
    var ENDLIB
    var ENDMASKS
    var ENDSTR
    var FONTS
    var FORMAT
    var GENERATIONS
    var HARDFENCE
    var HARDWIRE
    var HEADER
    var LAYER
    var LIBDIRSIZE
    var LIBNAME
    var LIBSECUR
    var LINKKEYS
    var LINKTYPE
    var MAG
    var MASK
    var NODE
    var NODEPORT
    var NODETYPE
    var PATH
    var PATHPORT
    var PATHTYPE
    var PLEX
    var PRESENTATION
    var PROPATTR
    var PROPVALUE
    var REFLIBS
    var RESERVED
    var SNAME
    var SOFTFENCE
    var SOFTWIRE
    var SPACER_ERROR
    var SPACING
    var SREF
    var SRFNAME
    var STRANS
    var STRCLASS
    var STRING
    var STRNAME
    var STRTYPE
    var STYPTABLE
    var TAPECODE
    var TAPENUM
    var TEXT
    var TEXTNODE
    var TEXTTYPE
    var UINTEGER
    var UNITS
    var USERCONSTRAINT
    var USTRING
    var WIDTH
    var XY

GDSTransform
++++++++++++++

::
    
    class GDSTransform(reflection: bool = False, magnification: float = 1, rotation: float = 0)

GDSTransform(reflection: bool = False, magnification: float = 1, rotation: float = 0)

Class variables
_________________

::
    
    var magnification: float
    var reflection: bool
    var rotation: float

GDSTransformFlag
+++++++++++++++++++

::
    
    class GDSTransformFlag(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.IntFlag, builtins.int, enum.Flag, enum.Enum

Class variables
___________________

::
    
    var ABS_MAGNIFICATION
    var ABS_ROTATION
    var REFLECTION