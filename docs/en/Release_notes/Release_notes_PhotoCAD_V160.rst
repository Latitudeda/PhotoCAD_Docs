PhotoCAD V1.6.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In **PhotoCAD** version 1.6.0, more useful and powerful functions are added and updated, as well as enhancing performance, re-designing simulation method, and integration with **MaxOptics** FDTD simulation tool.

#. Integration with **MaxOptics** FDTD simulator, please see ``simulation.ffi.maxoptics.fdtd_simulation.runner``.

#. Remove unnecessary ``@dataclass`` decorators.

#. Merge ``fnpcell.whl`` and ``gpdk.whl`` to ``photocad.whl``.

#. Re-designed simulation method, please see the following examples.

   #. ``example_sim_freqdomain.py``

   #. ``simulation/sim_model/*.py`` to create frequency domain simulation models (S-Matrix).

   #. ``examples/demux_1490/example_*.py`` freq-domain simulation demo of a cascaded Mach-Zehnder filter.

#. More examples provided to users with greater levels of support.

   #. ``components/bend/fixed_bend_euler_90.py`` Import GDS fixed cell as PCell, including scripting JSon file.

   #. ``example_pcell_custom.py`` Define the PCell class by adding parameters, which can be further use as the base PCell for all components or circuits.

   #. ``example_ports_ops.py`` How to get the information of ports in a cell, including specific coordinates, order, name, orientation.

   #. ``example_link_between_end_factory.py`` Allow users to define the start and end section in ``LinkBetween``, which can be a specific taper, bend, or transition.

   #. ``example_pcell_name_policy.py`` Demonstrate the policy of a PCell name in different scenario.

   #. ``example_line_cap.py`` Add ``line_cap`` parameter to make a round cap in ``PolyLine``.

   #. ``example_array_mzi2.py`` Demo the  use ``new_array()`` function to reduce complexity and improve performance.

   #. ``examples/example_export_jsons.py`` Allow use to export multiple json files.

#. Some minor changes.

   #. ``wg.csv`` and ``wg_bends.csv`` for clearer clarity of the WG and bends using in WG.

   #. Replace ``end_hints`` to ``fp.el.LineCapButt``.

   #. Change default font to ``std_vented``.

   #. Update method to generate csv to ``layer.py`` & ``display.py``.















Dear users, you can now contact support@latitudea.com to get the PhotoCAD V1.6.0 software to experience the above update.

