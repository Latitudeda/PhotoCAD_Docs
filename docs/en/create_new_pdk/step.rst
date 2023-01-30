Steps
^^^^^^^^^^^^^^^^^^^^^^^^

1. Fill in layer discription based on foundry's manual in technology/layers.csv. Note that ``name`` & ``process`` row cannot include blank or parantheses.
2. run ``technology/gererate_layers_and_displays_from_csv.py``, then a new file will be generated under ``technology`` file. Copy ``layers.py`` & ``display.py`` in ``generated`` file and paste it in ``technology``.
3. Adjust ``technology/wg`` 
4. Adjust ``technology/ _init_.py``
5. Adjust ``technology/tech``
6. Adjust ``component/transition`` them ``technology/auto_transition``
