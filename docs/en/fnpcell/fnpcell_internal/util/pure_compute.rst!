Module fnpcell.internal.util.pure_compute
===========================================

Functions
------------

pure_compute
++++++++++++++

::
    
    def pure_compute(fn: Callable[[], ~_T], *, deps: Tuple[Hashable[], ...], threshold: float = 0) -> ~_T

Returns result of fn(), cache it if duration > threshold(in seconds), using deps as cache key.