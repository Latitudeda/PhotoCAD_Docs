Module fnpcell.pdk.technology.auto_vias
==========================================

Classes
----------

AutoVias
++++++++++

::
    
    class AutoVias(registry: Optional[Mapping[Union[Tuple[IMetalLineType, IMetalLineType], 
                    Tuple[Type[IMetalLineType], Type[IMetalLineType]]], Union[Callable[[], IViasFactory], 
                    Callable[[Tuple[IMetalLineType, IMetalLineType]], IViasFactory]]]] = None, /)

Registry for auto transition, used in fp.Linked / fp.LinkBetween / fp.LinkSmooth.

Usage::
    
    # (see gpdk.technology.auto_transition)

    from fnpcell.pdk.technology import all as fpt
    from gpdk.technology import WaveguideType
    from gpdk.components.transition.swg2mwg_transition import SWG2MWGTransition

    def _swg2mwg(types: Tuple[fpt.IMetalLineType, fpt.IMetalLineType]):
        return SWG2MWGTransition(name="auto", swg_length=10, mwg_length=10, swg_type=types[0], mwg_type=types[1])

    auto_transition = fpt.AutoVias()
    auto_transition += WaveguideType.SWG.C >> WaveguideType.MWG.C, _swg2mwg

Ancestors
___________

::
    
    IAutoVias

Instance variables
_____________________

::
    
    var DEFAULT

Methods
________

::
    
    def get(self, key: Tuple[-_S, -_D], default: Optional[IViasFactory] = None) -> Optional[IViasFactory]

::
    
    def updated(self, entries: Sequence[Union[Tuple[Tuple[-_S, -_D], Callable[[], IViasFactory]], 
                Tuple[Tuple[Type[-_S], Type[-_D]], Callable[[Tuple[-_S, -_D]], IViasFactory]]]])