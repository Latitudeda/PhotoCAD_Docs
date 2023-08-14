Simplify layout by ``use_sketch_view``
==============================================================================

In this section, we will introduce the function ``fp.use_sketch_view`` to help users become more efficiently when designing layouts. In a complicate photonic circuit, often building up with tens or hundreds of components, it is easy to face the situation that we need huge amount of time to generate GDS file but only want to see a small part of change in the circuit. The real case is that when implementing the waypoints or waylines between two components, we don't even care about what the components really looks like but focus on the connection between the ports.

The function ``fp.use_sketch_view`` captures the geometry of every layer of the cell and simplify them into one single layer. During the first time of generating GDS file opening ``fp.use_sketch_view``, ```PhotoCAD``` will automatically generate a sketch-view GDS file and JSon file indicating ports and layers information of the cell. After that, the formation of the GDS file of the circuit will based on the sketch-view GDS file and the non-sketch view cells.

Here is an example of using ``fp.use_sketch_view`` in a MZM circuit, containing three MZIs with pn phase shifter on the top arm. The three MZIs are totally different and are all GDS imported cell.

* mzm_l_200_pn_25 (length difference between two arms: 200 um, pn junction of the phae shifter: 25um)

  * y_splitter_taper_1 (splitter with

  * y_combiner_taper_1

  * phaseshifter_pn25

  .. image:: ../images/mzm_l_200_pn_25.png

* mzm_l_300_pn_50 (length difference between two arms: 300 um, pn junction of the phae shifter: 50um)

  * y_splitter_taper_5

  * y_combiner_taper_5

  * phaseshifter_pn50

  .. image:: ../images/mzm_l_300_pn_50.png


* mzm_l_400_pn_75 (length difference between two arms: 400 um, pn junction of the phae shifter: 75um)

  * y_splitter_taper_10

  * y_combiner_taper_10

  * phaseshifter_pn75

  .. image:: ../images/mzm_l_400_pn_75.png






* Useful when generating large area of layout but only want to focus on the connections between ports rather than the cell itself.

* Write ``fp.use_sketch_view(device, sketch_layer, conf)`` before exporting GDS file.

* For more information please see section Sketch view of PCells.





