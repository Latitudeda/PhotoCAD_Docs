Steps
^^^^^^^^^^^^^^^^^^^^^^^^

1. Fill in layer discription based on foundry's manual in technology/layers.csv. Note that ``name`` & ``process`` row cannot include blank or parantheses.
2. run ``technology/gererate_layers_and_displays_from_csv.py``, then a new file will be generated under ``technology`` file. Copy ``layers.py`` & ``display.py`` in ``generated`` file and paste it in ``technology``.
3. Adjust ``technology/wg`` 
4. Adjust ``technology/ _init_.py``
5. Adjust ``technology/tech``
6. Adjust ``component/transition`` then ``technology/auto_transition``
7. Adjust ``component/via/via&vias`` then ``technology/auto_vias``

8. Import foundry gds file, then create json file (name=foundry gds file name) & .py file (name= fixed+foundry gds file name).

9. component/Straight, taper, bend, splitter, sbend, dc, ringresonator, ring filter, mzi, mmi, metal_taper, tinheater, gc, bondpad 
