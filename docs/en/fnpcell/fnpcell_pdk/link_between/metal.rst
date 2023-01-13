Module fnpcell.pdk.link_between.metal
=======================================

Functions
-------------

new_metal_line_between
++++++++++++++++++++++++

::
    
    def new_metal_line_between(start: ITerminal, end: ITerminal, *, 
                                waypoints: Iterable[Union[IRay, Offset]] = (), min_distance: Optional[float] = None, 
                                start_distance: Optional[float] = None, end_distance: Optional[float] = None, 
                                metal_line_type: Union[None, IMetalLineType, Iterable[Tuple[float, IMetalLineType]]] = None, 
                                fitting_function: Optional[Callable[[Tuple[Tuple[float, float], ...]], ICurve]] = None, 
                                auto_vias: Optional[AutoVias] = None, flyline_layer: Optional[ILayer] = None, 
                                target_length: Optional[float] = None, transform: Affine2D = Affine2D.identity(), 
                                name: str = 'LinkBetween') -> Optional[fnpcell_autolink.link_between.metal.MetalLineBetween]

This function is used to automatically link two pins.

Args

waypoints::
    
    to appoint the auto link's waypoint that auto link go through.

min_distance::
    
    default minimum distance before turning around.

start_distance::
    
    default minimum distance (from start port) before turning around.

end_distance::
    
    default minimum distance (from end port) before turning around.

metal_line_type::
    
    a registry contains metal line type for a specific layer.

auto_vias::
    
    a registry contains functions which generate vias for a specific layer pair.

flyline_layer::
    
    the flyline layer. If the link fails, a flyline is created between the ports.

target_length::
    this link's length.

Usage::
    
    fp.LinkBetween(start=cell1["ep_1"], end=cell2["ep_0"], start_distance=40, 
                    metal_line_type=[(0, TECH.METAL.MT.W10)],)

Returns

An instance of LinkBetween or None when start and end matches directly.