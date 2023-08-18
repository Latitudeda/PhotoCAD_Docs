Simplify layout by ``fp.use_sketch_view``
==============================================================================

In this section, we will introduce the function ``fp.use_sketch_view`` to help users become more efficiently when designing layouts. In a complicate photonic circuit, often building up with tens or hundreds of components, it is easy to face the situation that we need huge amount of time to generate GDS file but only want to see a small part of change in the circuit. The real case is that when implementing the waypoints or waylines between two components, we don't even care about what the components really looks like but focus on the connection between the ports.

The function ``fp.use_sketch_view`` captures the geometry of every layer of the cell and simplify them into one single layer. During the first time of generating GDS file opening ``fp.use_sketch_view``, ```PhotoCAD``` will automatically generate a sketch-view GDS file and JSon file indicating ports and layers information of the cell. After that, the formation of the GDS file of the circuit will based on the sketch-view GDS file and the non-sketch view cells.

Here is an example of using ``fp.use_sketch_view`` in a MZM circuit, containing three MZIs with pn phase shifter on the top arm. The three MZIs are totally different and are all GDS imported cell.

* mzm_l_200_pn_25 (length difference between two arms: 200 um, pn junction of the phase shifter: 25um)

  * y_splitter_taper_1

  * y_combiner_taper_1

  * phaseshifter_pn25

  .. image:: ../images/mzm_l_200_pn_25.png

* mzm_l_300_pn_50 (length difference between two arms: 300 um, pn junction of the phase shifter: 50um)

  * y_splitter_taper_5

  * y_combiner_taper_5

  * phaseshifter_pn50

  .. image:: ../images/mzm_l_300_pn_50.png


* mzm_l_400_pn_75 (length difference between two arms: 400 um, pn junction of the phase shifter: 75um)

  * y_splitter_taper_10

  * y_combiner_taper_10

  * phaseshifter_pn75

  .. image:: ../images/mzm_l_400_pn_75.png

* Connect three MZIs

  .. image:: ../images/topcircuit.png

Implement ``fp.use_sketch_view``
--------------------------------------------

* ``conf = fp.SketchConf(sketch_layer=TECH.LAYER.TEXT_NOTE, marker_layer=TECH.LAYER.FLYLINE_MARK)``

  The configuration parameter sets the sketched cell to the designated layer. The example code above will assign the sketched cell to ``TEXT_NOTE`` layer, and by the ``marker_layer`` will show the direction of the ports with an arrow.

  * ``sketch_layer``

    .. image:: ../images/topcircuit1.png

  * ``marker_layer``

    .. image:: ../images/topcircuit2.png

* ``fp.use_sketch_view(mzm_l_200_pn_25, conf=conf)``

  The first parameter of ``fp.use_sketch_view`` reads the cell which will be sketched. It could be any level of the circuit.

Different usage of ``fp.use_sketch_view``
-------------------------------------------

* Sketch all MZMs

  ::

        fp.use_sketch_view(mzm_l_200_pn_25, conf=conf)
        fp.use_sketch_view(mzm_l_300_pn_50, conf=conf)
        fp.use_sketch_view(mzm_l_400_pn_75, conf=conf)

  .. image:: ../images/topcircuit_mzm.png


* Sketch all Phase Shifters

  ::

        fp.use_sketch_view(phaseshifter_pn25, conf=conf)
        fp.use_sketch_view(phaseshifter_pn50, conf=conf)
        fp.use_sketch_view(phaseshifter_pn75, conf=conf)

  .. image:: ../images/topcircuit_ps.png


* Sketch all Combiners

  ::

        fp.use_sketch_view(y_combiner_taper1, conf=conf)
        fp.use_sketch_view(y_combiner_taper5, conf=conf)
        fp.use_sketch_view(y_combiner_taper10, conf=conf)

  .. image:: ../images/topcircuit_combiner.png


* Sketch only the first MZM

  ::

        fp.use_sketch_view(mzm_l_200_pn_25, conf=conf)

  .. image:: ../images/topcircuit_mzmonly1.png


GDS file build-time results
-------------------------------------

We track the build-up time of the GDS file when implementing different scenarios.

* Circuit without any sketch view: 0.1482s

* 1st time open all MZMs sketch view: 0.1423s

* 2nd time open all MZMs sketch view: 0.0654s

* Close all sketch view: 0.1529s

* 3rd time open all MZMs sketch view: 0.0659s

* 1st time open child cell (all phase shifters) sketch view: 0.1594s

* 2nd time open child cell (all phase shifters) sketch view: 0.1385s

* Close all child cell sketch view: 0.1483s

From the above results we can see that ``fp.use_sketch_view`` increases two to three times the speed of generating the GDS file. First time opening the sketch view needs some time to generate the GDS and Json files of the sketched cell, but after that the build-up time can be efficiently saved.







