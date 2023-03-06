Module fnpcell.pdk.linked
============================

Functions
-----------

Linked
++++++++

::
    
    def Linked(*, name: str = 'Linked', flyline_layer: Optional[ILayer] = None, 
                linking_policy: Optional[LinkingPolicy] = None, link_type: Optional[IWaveguideType] = None, 
                straight_factory: Optional[IStraightWaveguideFactory] = None, 
                bend_factory: Optional[IBendWaveguideFactory] = None, 
                links: Iterable[Union[None, IWaveguideBetween, IMetalLineBetween, Tuple[IOwnedTerminal, 
                IOwnedTerminal], Tuple[Tuple[IOwnedTerminal, IOwnedTerminal], Optional[float]], 
                Waypoints[IOwnedTerminal, IOwnedTerminal], Tuple[Waypoints[IOwnedTerminal, IOwnedTerminal], 
                Optional[float]], Iterable[Union[None, IWaveguideBetween, IMetalLineBetween, 
                Tuple[IOwnedTerminal, IOwnedTerminal], Tuple[Tuple[IOwnedTerminal, IOwnedTerminal], 
                Optional[float]], Waypoints[IOwnedTerminal, IOwnedTerminal], 
                Tuple[Waypoints[IOwnedTerminal, IOwnedTerminal], Optional[float]]]]]], 
                metal_min_distance: Optional[float] = None, metal_start_distance: Optional[float] = None, 
                metal_end_distance: Optional[float] = None, 
                metal_line_type: Union[None, IMetalLineType, 
                Iterable[Tuple[float, IMetalLineType]]] = None, 
                metal_fitting_function: Optional[Callable[[Tuple[Tuple[float, float], ...]], ICurve]] 
                = None, auto_vias: Optional[AutoVias] = None, ports: Iterable[ITerminal], 
                transform: Affine2D = Affine2D.identity()) -> ICellRef

Create links between ports and returns an device including all used devices and generated links.

Args

name::
    
    default to "Linked", the name of generated cell

flyline_layer::
    
    Optional, flyline is generated if there's no spacing to insert bend/transition/taper etc. If absent, default to use TECH.LAYER.FLYLINE_MARK

linking_policy::
    
    Optional, providing default link_type and default bend_factory for each port pairs. If absent, TECH.LINKING_POLICY.DEFAULT will be used.

link_type::
    
    Optional, waveguide type to be used to generate waveguide links. LinkBetween has a parameter link_type which has priority over Linked()'s link_type.

bend_factory::
    
    Optional, a factory function to generate bend.

links::

    like this

    [cell1["op_0"] >> cell2["op_0"], cell1["op_1"] >> cell2["op_1"],] or [cell1["op_0"] >> to(750, 300, 0) >> cell1["op_0"],]

metal_line_width::
    
    Optional, default line width of metal line links which are generated from pin pairs. 
    If absent, default to use TECH.METAL.DEFAULT_LINE_WIDTH

metal_min_distance::
    
    Optional, default minimum distance before turning around. LinkBetween has a parameter 
    min_distance which has priority over metal_min_distance. AssertionError will be raised 
    if neither min_distance nor metal_min_distance is provided

metal_start_distance::
    
    Optional, default minimum distance (from start port) before turning around. 
    LinkBetween has a parameter start_distance which has priority over metal_start_distance. 
    AssertionError will be raised if neither start_distance nor metal_start_distance is provided

metal_end_distance::
    
    Optional, default minimum distance (from end port) before turning around. 
    LinkBetween has a parameter end_distance which has priority over metal_end_distance. 
    AssertionError will be raised if neither end_distance nor metal_end_distance is provided

metal_via_spacing::
    
    Optional, default via spacing. This affects how vias are inserted: less vias for larger 
    via spacing LinkBetween has a parameter via_spacing which has priority over metal_via_spacing. 
    AssertionError will be raised if neither via_spacing nor metal_via_spacing is provided

metal_overlap_distance::
    
    Optional, default overlap distance when metal line go to another layer. 
    This affects how vias are inserted: more vias for larger overlap distance 
    LinkBetween has a parameter overlap_distance which has priority over metal_overlap_distance. 
    AssertionError will be raised if neither overlap_distance nor metal_overlap_distance is provided

auto_vias::
    
    Optional, a registry contains functions which generate vias for a specific layer pair. 
    LinkBetween has a parameter auto_vias which has priority over Linke's auto_vias.
     AssertionError will be raised if neither is provided

auto_metal_line_type::
    
    Optional, a registry contains metal line type for a specific layer. 
    LinkBetween has a parameter auto_metal_line_type which has priority over Linke's auto_metal_line_type. 
    AssertionError will be raised if neither is provided

ports::
    
    Required, public ports of the

transform::
    
    Optional, transform of the generated device

Returns

An ICellRef/IDevice including the generated links and source devices whose ports 
are used to generate the links. Usage::
    
    device_linked = fp.Linked(
        link_type=TECH.WG.MWG.C.WIRE,
        bend_factory=TECH.WG.MWG.C.WIRE.BEND_CIRCULAR,
        links=[
            cell1["op_0"] >> cell2["op_0"],
        ],
        ports=[
            cell1["op_1"].with_name("op_0"),
            cell2["op_1"]
        ]
    )