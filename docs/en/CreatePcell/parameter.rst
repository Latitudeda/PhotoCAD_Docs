Default values for PCell Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ways to implement default values for PCell parameter
=======================================================

* default: assign a default value in ``fp.FloatParam``.

   ``length: float = fp.FloatParam(default=6)``

* default_factory: assign a function that returns a value which is used to be a parameter here.


``length: float = fp.FloatParam(default_factory=)``

* `_default_xxx` method:


