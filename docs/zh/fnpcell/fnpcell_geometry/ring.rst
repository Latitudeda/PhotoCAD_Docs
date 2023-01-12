Module fnpcell.geometry.ring
==============================

Functions
-----------

new_ring
++++++++++

::
    
    def new_ring(outer_radius: float, inner_radius: float = 0, 
                    initial_radians: Union[None, float, Iterable[float]] = None, 
                    initial_degrees: Union[None, float, Iterable[float]] = None, 
                    final_radians: Union[None, float, Iterable[float]] = None, 
                    final_degrees: Union[None, float, Iterable[float]] = None, 
                    origin: Optional[Tuple[float, float]] = None, 
                    transform: Affine2D = Affine2D.identity()) -> EllipticalRing
                    
Create a CircularRing.