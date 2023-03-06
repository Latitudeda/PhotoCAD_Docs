Module fnpcell.internal.util.waypoint_util
============================================

Functions
----------

resolve_waypoints
+++++++++++++++++++++

::
    
    def resolve_waypoints(start: IRay, end: IRay, radius_eff: Callable[[float], float], 
                            waypoints: Iterable[Union[IRay, Offset]]) -> Tuple[IRay, ...]

Plans a new specified path connecting the start and end based on the waypoints between the start and end, 
the new specified path is all composed of coordinate points with direction, and then these coordinate 
points with direction are connected in sequence to complete the final path of start and end.

Args

start
    start point with direction

end
    end point with direction

radius_eff
    radius effective

waypoints
    waypoints to be passed between start and end