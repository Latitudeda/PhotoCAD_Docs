Module fnpcell.pdk.link_between.wg
=====================================

Functions
------------

::
    
    def new_waveguide_between(start: ITerminal, end: ITerminal, *, 
                                waypoints: Iterable[Union[IRay, Offset]] = (), 
                                linking_policy: Optional[LinkingPolicy] = None, 
                                link_type: Optional[IWaveguideType] = None, 
                                straight_factory: Optional[IStraightWaveguideFactory] = None, 
                                bend_factory: Optional[IBendWaveguideFactory] = None, 
                                flyline_layer: Optional[ILayer] = None, 
                                target_length: Optional[float] = None, 
                                transform: Affine2D = Affine2D.identity(), 
                                name: str = 'LinkBetween') -> Optional[fnpcell_autolink.link_between.wg.WaveguideBetween]

LinkBetween function.

this function is used to link two ports auto link.

Args

waypoints::
    
    to appoint the auto link's waypoint that auto link go through.

link_type::
    
    which waveguide type be used to this link.

bend_type::
    
    which bend's waveguide type be used to this link.

target_length::
    
    this link's length.

flyline_layer::
    
    the flyline layer. If the link fails, a flyline is created between the ports.

Usage::
    
    fp.LinkBetween(start=cell1["op_1"], end=cell2["op_0"], bend_factory=TECH.WG.MWG.C.WIRE.BEND_EULER)

Returns

An instance of LinkBetween or None when start and end matches directly.
