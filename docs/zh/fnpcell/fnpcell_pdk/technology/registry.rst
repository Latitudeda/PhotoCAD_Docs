Module fnpcell.pdk.technology.registry
=========================================

Functions
-----------

angle_step
++++++++++++

::
    
    def angle_step() -> float

Returns the step angle units of current technology in radians.

get_technology
++++++++++++++++

::
    
    def get_technology(default_tech: Type[Any] = fnpcell.pdk.technology.tech.ITech, /, 
                        warnings: Optional[bool] = None) -> Any

grid_unit
+++++++++++

::
    
    def grid_unit() -> float

Returns grid of current technology in meters.

register_technology
++++++++++++++++++++++

::
    
    def register_technology(tech: Type[~_T], /, 
                            warnings: Optional[bool] = None) -> Callable[[], Type[~_T]]

Register technology as the current technology.

Usage::
    
    # (gpdk/technology/init.py)

    from .tech import TECH as _TECH

    register_technology(_TECH)

snap_scale
+++++++++++++

::
    
    def snap_scale() -> float

Returns snap scale (=round(1 / grid_unit()) / round(1 / user_unit())) in current technology.

user_unit
++++++++++++

::
    
    def user_unit() -> float

Returns user unit of current technology in meters.