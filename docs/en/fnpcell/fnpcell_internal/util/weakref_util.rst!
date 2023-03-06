Module fnpcell.internal.util.weakref_util
=============================================

Classes
---------

WeakKeyValueDictionary
++++++++++++++++++++++++++

::
    
    class WeakKeyValueDictionary

Abstract base class for generic types.

A generic type is typically declared by inheriting from this class parameterized with one or more type variables. 
For example, a generic mapping type might be defined as::
    
    class Mapping(Generic[KT, VT]): 
        def getitem(self, key: KT) -> VT: … # Etc.

This class can then be used as follows::
    
    def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT: 
        try: return mapping[key] 
        except KeyError: return default

Ancestors
____________

::
    
    typing.Generic, weakref.WeakKeyDictionary, collections.abc.MutableMapping, 
    collections.abc.Mapping, collections.abc.Collection, collections.abc.Sized, 
    collections.abc.Iterable, collections.abc.Container

Methods
____________

::
    
    def get(self, key: ~_K, default: Optional[~_V] = None) -> Optional[~_V]
    
D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.