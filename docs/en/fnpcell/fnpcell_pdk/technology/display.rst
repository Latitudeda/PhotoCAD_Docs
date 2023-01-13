Module fnpcell.pdk.technology.display
=======================================

Classes
----------

Color
++++++++

::
    
    class Color(r: float, g: float, b: float, a: float = 1)

Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple. 
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.

Ancestors
____________

::
    
    builtins.tuple, typing.Generic

Subclasses
____________

::
    
    .NamedColor

Methods
_________

::
    
    def with_alpha(self, alpha: float)

FillPattern
+++++++++++++

::
    
    class FillPattern(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
____________

::
    
    enum.Enum

Class variables
__________________

::
    
    var BACK_DIAGONAL
    var DIAGONAL
    var DOTTED
    var GRID
    var HOLLOW
    var SOLID

LayerFill
++++++++++++

::
    
    class LayerFill(color: Color, pattern: FillPattern)

LayerFill(color: fnpcell.pdk.technology.display.Color, pattern: fnpcell.pdk.technology.display.FillPattern)

Class variables
__________________

::
    
    var color : Color
    var pattern : FillPattern

LayerStroke
+++++++++++++

::
    
    class LayerStroke(width: float, color: Color)

LayerStroke(width: float, color: fnpcell.pdk.technology.display.Color)

Class variables
__________________

::
    
    var color: Color
    var width: float

LayerStyle
+++++++++++++

::
    
    class LayerStyle(fill: LayerFill, stroke: LayerStroke)

LayerStyle(fill: fnpcell.pdk.technology.display.LayerFill, stroke: fnpcell.pdk.technology.display.LayerStroke)

Class variables
_________________

::
    
    var fill: LayerFill
    var stroke: LayerStroke

LayerStyleSet
++++++++++++++++

::
    
    class LayerStyleSet(registry: Optional[Mapping[ILayer, LayerStyle]] = None, /)

Static methods
_________________

::
    
    def random(layers: Sequence[ILayer])

Methods
_________

::
    
    def get(self, key: ILayer, default: Optional[LayerStyle] = None) -> Optional[LayerStyle]

::
    
    def updated(self, value: Mapping[ILayer, LayerStyle], /)

NamedColor  
++++++++++++

::
    
    class NamedColor(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

Ancestors
____________

::
    
    Color builtins.tuple, typing.Generic, enum.Enum

Class variables
__________________

::
    
    var ALICEBLUE
    var ANTIQUEWHITE
    var AQUAMARINE
    var AZURE
    var BEIGE
    var BISQUE
    var BLACK
    var BLANCHEDALMOND
    var BLUE
    var BLUEVIOLET
    var BROWN
    var BURLYWOOD
    var CADETBLUE
    var CHARTREUSE
    var CHOCOLATE
    var CORAL
    var CORNFLOWERBLUE
    var CORNSILK
    var CRIMSON
    var CYAN
    var DARKBLUE
    var DARKCYAN
    var DARKGOLDENROD
    var DARKGRAY
    var DARKGREEN
    var DARKKHAKI
    var DARKMAGENTA
    var DARKOLIVEGREEN
    var DARKORANGE
    var DARKORCHID
    var DARKRED
    var DARKSALMON
    var DARKSEAGREEN    
    var DARKSLATEBLUE
    var DARKSLATEGRAY
    var DARKTURQUOISE
    var DARKVIOLET
    var DEEPPINK
    var DEEPSKYBLUE
    var DIMGRAY
    var DODGERBLUE
    var FIREBRICK
    var FLORALWHITE
    var FORESTGREEN
    var FUCHSIA
    var GAINSBORO
    var GHOSTWHITE
    var GOLD    
    var GOLDENROD
    var GRAY
    var GREEN
    var GREENYELLOW
    var HONEYDEW
    var HOTPINK
    var INDIANRED
    var INDIGO
    var IVORY
    var KHAKI
    var LAVENDER
    var LAVENDERBLUSH
    var LAWNGREEN
    var LEMONCHIFFON
    var LIGHTBLUE
    var LIGHTCORAL
    var LIGHTCYAN
    var LIGHTGOLDENRODYELLOW
    var LIGHTGRAY
    var LIGHTGREEN
    var LIGHTPINK   
    var LIGHTSALMON 
    var LIGHTSEAGREEN
    var LIGHTSKYBLUE
    var LIGHTSLATEGRAY
    var LIGHTSTEELBLUE
    var LIGHTYELLOW
    var LIMEGREEN
    var LINEN   
    var MAGENTA 
    var MAROON
    var MEDIUMAQUAMARINE    
    var MEDIUMBLUE
    var MEDIUMORCHID
    var MEDIUMPURPLE
    var MEDIUMSEAGREEN
    var MEDIUMSLATEBLUE
    var MEDIUMSPRINGGREEN
    var MEDIUMTURQUOISE
    var MEDIUMVIOLETRED
    var MIDNIGHTBLUE
    var MINTCREAM
    var MISTYROSE
    var MOCCASIN
    var NAVAJOWHITE 
    var NAVY    
    var OLDLACE
    var OLIVE
    var OLIVEDRAB
    var ORANGE
    var ORANGERED
    var ORCHID
    var PALEGOLDENROD
    var PALEGREEN
    var PALETURQUOISE
    var PALEVIOLETRED   
    var PAPAYAWHIP  
    var PEACHPUFF   
    var PERU
    var PINK    
    var PLUM    
    var POWDERBLUE  
    var PURPLE  
    var REBECCAPURPLE   
    var RED
    var ROSYBROWN
    var ROYALBLUE
    var SADDLEBROWN 
    var SALMON
    var SANDYBROWN  
    var SEAGREEN
    var SEASHELL
    var SIENNA
    var SILVER
    var SKYBLUE
    var SLATEBLUE
    var SLATEGRAY   
    var SNOW
    var SPRINGGREEN
    var STEELBLUE
    var TAN
    var TEAL
    var THISTLE
    var TOMATO
    var TURQUOISE
    var VIOLET
    var WHEAT
    var WHITE
    var WHITESMOKE
    var YELLOW
    var YELLOWGREEN