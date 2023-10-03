Directional Coupler Bend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Full script
-----------------------------------------------

::

  from dataclasses import dataclass
  from typing import Tuple, cast
  from fnpcell import all as fp
  from gpdk.components.bend.bend_circular import BendCircular
  from gpdk.components.straight.straight import Straight
  from gpdk.technology import get_technology
  from gpdk.technology.interfaces import CoreCladdingWaveguideType

  @fp.pcell_class()

  class DirectionalCouplerBend(fp.PCell):
      coupler_spacing: float = fp.PositiveFloatParam(default=0.7, doc="Spacing between the two waveguide centre lines.").as_field()
      coupler_length: float = fp.PositiveFloatParam(default=6, doc="Length of the directional coupler").as_field()
      bend_radius: float = fp.PositiveFloatParam(required=False, doc="Bend radius for the auto-generated bends").as_field()
      straight_after_bend: float = fp.PositiveFloatParam(default=6, doc="Length of the straight waveguide after the bend").as_field()
      waveguide_type: CoreCladdingWaveguideType = fp.WaveguideTypeParam(type=CoreCladdingWaveguideType, doc="Waveguide parameters").as_field()
      port_names: fp.IPortOptions = fp.PortOptionsParam(count=4, default=["op_0", "op_1", "op_2", "op_3"]).as_field()

      def _default_waveguide_type(self):
          return get_technology().WG.FWG.C.WIRE

      def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
          insts, elems, ports = super().build()
          # fmt: off
          coupler_spacing = self.coupler_spacing
          coupler_length = self.coupler_length
          bend_radius = self.bend_radius
          straight_after_bend = self.straight_after_bend
          waveguide_type = self.waveguide_type
          port_names = self.port_names

          if bend_radius is None:
              bend_radius = cast(float, waveguide_type.BEND_CIRCULAR.radius_eff) # type: ignore

          assert (
              coupler_spacing > waveguide_type.core_width
          ), "waveguide core overlap: coupler spacing must be greater than core_width"

          dy = coupler_spacing / 2

          left_straight_after_bend = Straight(name="lafterbend", length=straight_after_bend, waveguide_type=waveguide_type)
          right_straight_after_bend = Straight(name="rafterbend", length=straight_after_bend, waveguide_type=waveguide_type)
          left_bend = BendCircular(name="lbend", degrees=90, radius=bend_radius, waveguide_type=waveguide_type)
          right_bend = BendCircular(name="rbend", degrees=90, radius=bend_radius, waveguide_type=waveguide_type)
          straight_coupler = Straight(name="coupler", length=coupler_length, anchor=fp.Anchor.CENTER, waveguide_type=waveguide_type, transform=fp.translate(0, -dy))

          bottom_half = fp.Connected(
              name="bottom",
              joints=[
                  straight_coupler["op_0"] <= left_bend["op_0"],
                  left_bend["op_1"] <= left_straight_after_bend["op_1"],
                  #
                  straight_coupler["op_1"] <= right_bend["op_1"],
                  right_bend["op_0"] <= right_straight_after_bend["op_0"],
              ],
              ports=[
                  left_straight_after_bend["op_0"],
                  right_straight_after_bend["op_1"],
              ],
          )
          insts += bottom_half
          top_half = bottom_half.rotated(degrees=180)
          insts += top_half
          ports += top_half["op_1"].with_name(port_names[0])
          ports += bottom_half["op_0"].with_name(port_names[1]),
          ports += bottom_half["op_1"].with_name(port_names[2]),
          ports += top_half["op_0"].with_name(port_names[3]),

          # fmt: on
          return insts, elems, ports

  if __name__ == "__main__":
      from pathlib import Path
      gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
      library = fp.Library()
      TECH = get_technology()
      # library += DirectionalCouplerBend()
      # library += DirectionalCouplerBend(name="f", coupler_spacing=0.7, coupler_length=6, bend_radius=10, straight_after_bend=6, waveguide_type=TECH.WG.FWG.C.WIRE)
      library += DirectionalCouplerBend(name="s", coupler_spacing=1.7, coupler_length=10, bend_radius=10, straight_after_bend=6, waveguide_type=TECH.WG.SWG.C.WIRE)

      fp.export_gds(library, file=gds_file)
      fp.plot(library)
      
      
Parameter description
----------------------------------------------------------------
In the main function, add a ``DirectionalCouplerBend`` to the library      

::

  library += DirectionalCouplerBend(name="s", coupler_spacing=1.7, coupler_length=10, bend_radius=10, straight_after_bend=6, waveguide_type=TECH.WG.SWG.C.WIRE)


``name`` is the name of the device, here named s, ``coupler_space``, ``coupler_length``, ``bend_radius`` and ``straight_after_bend`` are marked in the figure below, which is convenient to quickly understand which part of the device is controlled by each parameter.

.. image:: ../example_image/5.1.png
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
