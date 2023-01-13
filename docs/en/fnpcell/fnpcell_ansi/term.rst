Module fnpcell.ansi.term
==========================

Functions
-----------

print_ansi
++++++++++++

::
    
    def print_ansi(*args: str) -> None

style
++++++

::
    
    def style(color: Optional[Color] = None, background: Optional[Color] = None) -> str

Classes
--------

Color
+++++++

::
    
    class Color(value, names=None, *, module=None, qualname=None, type=None, start=1)
    
An enumeration.
        
Ancestors
____________

::

    enum.Enum


Class variables
___________________

::

    var BLACK   
    var BLUE
    var CYAN
    var DARK_GRAY
    var DEFAULT
    var GREEN
    var LIGHT_BLUE
    var LIGHT_CYAN
    var LIGHT_GRAY
    var LIGHT_GREEN
    var LIGHT_MAGENTA
    var LIGHT_RED
    var LIGHT_YELLOW
    var MAGENTA
    var RED
    var WHITE
    var YELLOW
