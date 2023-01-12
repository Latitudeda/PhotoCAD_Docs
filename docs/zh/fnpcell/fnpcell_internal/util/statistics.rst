Module fnpcell.internal.util.statistics
=========================================

Functions
-----------

statistics
+++++++++++++

::
    
    def statistics(value: IRunnable) -> Tuple[Tuple[Type[Any], float], ...]

Classes
---------

Statistics
+++++++++++

::
    
    class Statistics

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
_____________

::
    
    IProcessor

Instance variables
____________________

::
    
    var result

Methods
_____________

::
    
    def enter(self, target: IRunnable) -> bool

**Inherited from:** IProcessor.enter

Called before processing a target. Return True to continue processing child content. 
False to stop here and run exit for the target.

::
    
    def exit(self, target: IRunnable) -> None

**Inherited from:** IProcessor.exit

Called after processing a target.