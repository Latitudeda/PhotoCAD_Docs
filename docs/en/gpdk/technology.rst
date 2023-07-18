technology
===================================

File ``technology`` mainly stores some scripts related to the underlying layer.
The following is an introduction through the parts that will be used frequently. We recommend users follow the below order to configure their own ``technology`` settings.

1. :ref:`layers.csv`
2. :ref:`wg.py`
3. :ref:`waveguide factory.py`
4. :ref:`auto_transition.py`
5. :ref:`auto_transition.py` or ``linker.py``


The file ``layers.csv`` is a user configuration file, and the user-configured csv file can be automatically converted into ``layers.py`` and ``display.py`` files by the file ``generate_layers_and_display_from_csv.py``.

.. toctree::
   :hidden:

   layers_csv
   waveguide_factory_py
   wg_py
   auto_link_py
   auto_transition_py

