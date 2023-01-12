fnpcell.resource
=========================

Classes
---------

BinaryResource
++++++++++++++++

::
    
    class BinaryResource(file: Union[str, os.PathLike, io.IOBase], *, mode: OpenMode = OpenMode.READ)

BinaryIO.

Args
filename

    filename will be resolve as relative path from current pcell's defining folder

Usage::
    
    from fnpcell import all as fp
    
    with fp.BinaryResource("test.gds", mode=fp.OpenMode.TRUNCATE) as io:
        io.write(b"abcdefg")

Ancestors
____________

::
    
    fnpcell.resource._Resource, typing.Generic

Instance variables
____________________

::
    
    var mode: str

OpenMode
++++++++++

::
    
    class OpenMode(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
___________

::
    
    enum.Flag, enum.Enum

Class variables
____________________

::
    
    var APPEND
    var NEW
    var READ
    var TRUNCATE
    var UPDATE

ResourceRoot
_____________

::
    
    class ResourceRoot(value: pathlib.Path)

Class variables
___________________

::
    
    var value: pathlib.Path

Static methods
___________________

::
    
    def current() -> pathlib.Path

::
    
    def set_current(value: pathlib.Path) -> None

TextResource
++++++++++++++

::
    
    class TextResource(file: Union[str, os.PathLike, io.TextIOBase], *, mode: OpenMode = OpenMode.READ)

TextIO.

Args
filename

    filename will be resolve as relative path from current pcell's defining folder

Usage::
    
    from fnpcell import all as fp
    
    with fp.TextResource("test.txt", mode=fp.OpenMode.TRUNCATE) as io:
        io.write("abcdefg")

Ancestors
____________

::
    
    fnpcell.resource._Resource, typing.Generic

Instance variables
____________________

::
    
    var mode: str