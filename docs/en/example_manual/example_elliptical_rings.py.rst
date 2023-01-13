Example: Elliptical Rings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Full script
-----------------------------------

::

  from dataclasses import dataclass
  from fnpcell import all as fp
  from gpdk.technology import get_technology


  @fp.pcell_class()
  @dataclass(eq=False)
  class EllipticalRings(fp.PCell):
      def build(self):
          insts, elems, ports = super().build()
          # fmt: off
          TECH = get_technology()

          # elems += fp.el.EllipticalRing(outer_radius=(8, 10), inner_radius=(4, 5), initial_degrees=(0, 0), final_degrees=(180, 180), layer=TECH.LAYER.M1_DRW, origin=(0, 0))
          elems += fp.el.Ring(outer_radius=4, inner_radius=2, initial_degrees=(60, 30), final_degrees=(120, 150), layer=TECH.LAYER.M2_DRW, origin=(30, 0))
          # fmt: on
          return insts, elems, ports


  if __name__ == "__main__":
      from pathlib import Path

      gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
      library = fp.Library()

      TECH = get_technology()
      # =============================================================
      # fmt: off

      library += EllipticalRings()

      # fmt: on
      # =============================================================
      fp.export_gds(library, file=gds_file)
      fp.plot(library)
      
      
fp.el.Ring Description
------------------------------------------------------------
      
::

  elems += fp.el.Ring(outer_radius=4, inner_radius=2, initial_degrees=(0, 0), final_degrees=(180, 180), layer=TECH.LAYER.M2_DRW, origin=(30, 0))


As shown in the figure, initial_degrees is the angle between the starting end and the x-axis, final_degrees is the angle between the ending end and the x-axis, the left parameter in the parentheses is the angle parameter of the external circle, the right is the angle parameter of the internal circle; origin defines the location of the center of the whole ring.

In the following, we set the initial and end angles to (0, 30) and (150, 120), respectively. The following figure is obtained after running the script.


fp.el.EllipticalRing Description
------------------------------------------------------------

::

  elems += fp.el.EllipticalRing(outer_radius=(8, 10), inner_radius=(4, 5), initial_degrees=(0, 0), final_degrees=(180, 180), layer=TECH.LAYER.M1_DRW, origin=(0, 0))
  
  
We can get an elliptical ring after running the above script. The first parameter of outer_radius and inner_radius represents the semi-short axis of the ellipse, and the second parameter represents the semi-long axis of the ellipse. initial_degrees and final_degrees are used in the same way as in the Ring function, so we will not repeat them here.
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
