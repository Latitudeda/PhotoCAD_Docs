Module fnpcell.pdk.route
==========================

Functions
-----------

lengthen_route
++++++++++++++++

::
    
    def lengthen_route(waypoints: Sequence[Tuple[float, float]], 
                        delta_length: float) -> Tuple[Tuple[float, float], ...]

If the waypoints exist 180 degrees U-turn, 
adjust the length of both sides of the 180 degrees U-turn.

route
+++++++

::
    
    def route(start: IRay, end: IRay, radius_eff: Callable[[float], float], start_straight: float = 0, 
                end_straight: float = 0, min_straight: float = 0) -> Tuple[Tuple[float, float], ...]
                
Plan waypoints according to the Manhattan algorithm.