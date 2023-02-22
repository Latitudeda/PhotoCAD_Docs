Module fnpcell.internal.util.test_util
========================================

Functions
-----------

assert_angle_eq
+++++++++++++++++

::
    
    def assert_angle_eq(angle1: float, angle2: float, hint: str = '')

assert_point_eq
+++++++++++++++++

::
    
    def assert_point_eq(point1: Tuple[float, float], point2: Tuple[float, float], 
                        precision: Optional[float] = None)

assert_points_eq
+++++++++++++++++++

::
    
    def assert_points_eq(points1: Iterable[Tuple[float, float]], points2: Iterable[Tuple[float, float]], 
                            precision: Optional[float] = None)

cell_via_gds
++++++++++++++

::
    
    def cell_via_gds(cell: Union[ICell, ICellRef])

dummy_port
+++++++++++

::
    
    def dummy_port(*, name: str, position: Tuple[float, float], orientation: float, 
                    waveguide_type: IWaveguideType) -> ICellRef

Creates a combination of elements for a given port, which is useful for testing 
certain situations that only require the port to exist.

get_snap_precision
+++++++++++++++++++++

::
    
    def get_snap_precision() -> float

set_snap_precision
+++++++++++++++++++++

::
    
    def set_snap_precision(snap_precision: float) -> None

snap_point
++++++++++++

::
    
    def snap_point(point: Tuple[float, float], 
                    precision: Optional[float] = None) -> Tuple[float, float]

snap_points
+++++++++++++

::
    
    def snap_points(points: Iterable[Tuple[float, float]], 
                    precision: Optional[float] = None) -> Tuple[Tuple[float, float], ...]

snap_value
++++++++++++  

::
    
    def snap_value(value: float, precision: Optional[float] = None) -> float

Classes
----------

BytesIO
+++++++++

::
    
    class BytesIO(*args, **kwargs)

Buffered I/O implementation using an in-memory bytes buffer.

Ancestors
_____________

::
    
    _io.BytesIO _io._BufferedIOBase _io._IOBase

Methods
_________

::
    
    def close(self) -> None
    
Disable all I/O operations.

StringIO
++++++++++

::
    
    class StringIO(*args, **kwargs)

Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object. The newline argument is like the one of TextIOWrapper's constructor.

Ancestors
_____________

::
    
    _io.StringIO _io._TextIOBase _io._IOBase

Methods
_________

::
    
    def close(self) -> None
    
Close the IO object.

Attempting any further operation after the object is closed will raise a ValueError.

This method has no effect if the file is already closed.