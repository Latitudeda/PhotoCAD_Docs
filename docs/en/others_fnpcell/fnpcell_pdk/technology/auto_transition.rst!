Module fnpcell.pdk.technology.auto_transition
===============================================

Classes
----------

AutoTransition
+++++++++++++++

::
    
    class AutoTransition(registry: Optional[Mapping[Union[Tuple[IWaveguideType, IWaveguideType], 
                            Tuple[Type[IWaveguideType], Type[IWaveguideType]]], Union[Callable[[], 
                            Tuple[ICurvedCellRef, Tuple[str, str]]], Callable[[Tuple[IWaveguideType, IWaveguideType]], 
                            Tuple[ICurvedCellRef, Tuple[str, str]]]]]] = None, /)

Registry for auto transition, used in fp.Linked / fp.LinkBetween / fp.LinkSmooth.

Usage::
    
    # (see gpdk.technology.auto_transition)

    from fnpcell.pdk.technology import all as fpt
    from gpdk.technology import WaveguideType
    from gpdk.components.transition.swg2mwg_transition import SWG2MWGTransition

    def _swg2mwg(types: Tuple[fpt.IWaveguideType, fpt.IWaveguideType]):
        return SWG2MWGTransition(name="auto", swg_length=10, mwg_length=10, swg_type=types[0], mwg_type=types[1])

    auto_transition = fpt.AutoTransition()
    auto_transition += WaveguideType.SWG.C >> WaveguideType.MWG.C, _swg2mwg

Instance variables
____________________

::
    
    var DEFAULT

Methods
_________

::
    
    def get(self, key: Tuple[-_S, -_D], default: Optional[Tuple[ICurvedCellRef, 
            Tuple[str, str]]] = None) ‑> Optional[Tuple[ICurvedCellRef, Tuple[str, str]]]

::
    
    def updated(self, entries: Sequence[Union[Tuple[Tuple[-_S, -_D], Callable[[], 
                Tuple[ICurvedCellRef, Tuple[str, str]]]], Tuple[Tuple[Type[-_S], Type[-_D]], 
                Callable[[Tuple[-_S, -_D]], Tuple[ICurvedCellRef, Tuple[str, str]]]]]])

LossIndex
+++++++++++

::
    
    class LossIndex(compares: Optional[Set[Union[Tuple[Type[Any], Type[Any]], 
                    Tuple[IWaveguideType, IWaveguideType]]]] = None, /)

Define auto LossIndex.

Usage::
    
    gpdk/technology/auto_transition.py