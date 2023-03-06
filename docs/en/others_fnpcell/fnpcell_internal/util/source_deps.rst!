Module fnpcell.internal.util.source_deps
==========================================

Functions
------------

collect_deps
++++++++++++++

::
    
    def collect_deps(root_paths: Iterable[Union[str, pathlib.Path]], 
                        file_path: Union[str, pathlib.Path], *, 
                        imports: Optional[Dict[str, pathlib.Path]] = None, 
                        exclude: Optional[Set[str]] = None)

Classes
--------

DepsFinder
++++++++++++

::
    
    class DepsFinder(roots: Set[pathlib.Path], file: pathlib.Path, 
                        imports: Dict[str, pathlib.Path], exclude: Set[str])

A node visitor base class that walks the abstract syntax tree and calls a visitor function 
for every node found. This function may return a value which is forwarded by the visit method.

This class is meant to be subclassed, with the subclass adding visitor methods.

Per default the visitor functions for the nodes are 'visit\_' + class name of the node. 
So a TryFinally node visit function would be visit_TryFinally. This behavior can be changed 
by overriding the visit method. If no visitor function exists for a node (return value None) 
the generic_visit visitor is used instead.

Don't use the NodeVisitor if you want to apply changes to nodes during traversing. For this 
a special visitor exists (NodeTransformer) that allows modifications.

Ancestors
___________

::
    
    ast.NodeVisitor

Methods
__________

::
    
    def visit_Import(self, node: _ast.Import)

callback for 'import' statement.

::
    
    def visit_ImportFrom(self, node: _ast.ImportFrom)

callback for 'import from' statement.