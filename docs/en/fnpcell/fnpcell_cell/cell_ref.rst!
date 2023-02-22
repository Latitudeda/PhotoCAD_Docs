Module fnpcell.cell.cell_ref
================================

Functions
------------

create_cell_ref
+++++++++++++++++

::

    def create_cell_ref(*, name: Optional[str] = None,
                         content: Iterable[Union[None, IElement, ICell, ForwardRef('_T')]],
                         ports: Iterable[ITerminal], transform: Affine2D = Affine2D.identity()) -> ICellRef
    
Create a cell reference to a cell generated from name, content and ports.

Usage::

    from fnpcell import all as fp
    from gpdk.technology import get_technology

    if __name__ == "__main__":
        from pathlib import Path

        gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
        library = fp.Library()
        TECH = get_technology()

        # =======================================================================
        # fmt: off

        device = fp.Device(content=[fp.el.Line(length=10, stroke_width=2, layer=TECH.LAYER.MT_DRW)], ports=[])
        library += device

        # fmt: on
        # =============================================================
        fp.export_gds(library, file=gds_file)
        # fp.plot(library)

create_curved_cell_ref
+++++++++++++++++++++++

::

    def create_curved_cell_ref(*, curve: ICurve, name: Optional[str] = None,
                                 content: Iterable[Union[None, IElement, ICell, ForwardRef('_T')]],
                                  ports: Iterable[ITerminal], transform: Affine2D = Affine2D.identity()) -> ICurvedCellRef

Create a cell reference to a cell generated from name, content and ports.

Usage::

    from fnpcell import all as fp

    from gpdk.technology import get_technology

    if __name__ == "__main__":
        from pathlib import Path

        gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
        library = fp.Library()
        TECH = get_technology()

        # =======================================================================
        # fmt: off

        device = fp.CurvedDevice(
            curve=fp.g.line(length=10),
            content=[
                fp.el.Line(
                    length=10,
                    stroke_width=2,
                    layer=TECH.LAYER.MT_DRW,
                ),
            ],
            ports=[],
        )

        library += device

        # fmt: on
        # =============================================================
        fp.export_gds(library, file=gds_file)
        # fp.plot(library)

new_cell_ref
++++++++++++++++

::

    def new_cell_ref(cell: ICell, *, transform: Affine2D = Affine2D.identity()) -> ICellRef

Return a cell's reference.

Classes
--------

CellRef
+++++++++

::
    
    class CellRef

Define Cell Reference.

Ancestors
___________

::
    
    TransformMixin, ICellRef, IUpdatable, IElement, IRunnable, IAffineTransformable

Subclasses
____________

::

    fnpcell.cell.cell_ref._ImmutableCellRef,
    fnpcell.cell.cell_ref._ImmutableCurvedCellRef,
    MetalLine,
    Waveguide,
    fnpcell.pdk._pcell_fields.PCellFields,
    Flyline,
    LinkSmooth,
    fnpcell_autolink.link_between,metal.MetalLineBetween,
    fnpcell_autolink.link_between.wg.WaveguideBetween.

Class variables
_________________

::
    
    var cell: ICell
    var transform: Affine2D

Static methods
_________________

::
    
    def transform_from_at(at: Union[None, Tuple[float, float], IPositioned, IRay] = None,
                                 transform: Affine2D = Affine2D.identity()) -> Affine2D

**Inherited from:** TransformMixin.transform_from_at

Returns an Affine2D that is the result of the matrix product of the given transformation 
and the translation transformation at the given origin, the …

Instance variables
++++++++++++++++++++

::
    
    var ports

Return owned ports of the cell reference.

Methods
__________

::
    
    def c_mirrored(self: ~_Self, *, center: Tuple[float, float] = (0, 0)) -> ~_Self

**Inherited from:** TransformMixin.c_mirrored

Center mirrored.

::
    
    def content_merged(self, *, affected_layer: Iterable[ILayer])

Return a new cell reference with close elements on same layer merged into polygons.
Multiple layers can be provided and elements on each layer will be merged into polygons seperately.

examples::
    
    new_device = device.content_merged(affected_layer=TECH.LAYER.FWG_CORE)
    new_device = device.content_merged(affected_layer=[TECH.LAYER.FWG_CORE, TECH.LAYER.SWG_CORE])

::
    
    def flatten(self, depth: int = 1)

Return a new cell reference with transformed content and identity transform to itself. 
Useful to fix the "1nm gap" due to gds spec This method only flatten one level, 
not recursively flatten all content.
                
examples::
    
    new_device = device.flatten()
    
::
    
    def h_mirrored(self: ~_Self, *, x: float = 0) -> ~_Self

**Inherited from:** TransformMixin.h_mirrored

Horizontal mirrored.

::
    
    def new_array(self, *, cols: int = 1, col_width: float = 0, rows: int = 1, row_height: float = 0,
                             transform: Affine2D = Affine2D.identity())

Return a new cell reference array

::
    
    def polygon_set(self, *, layer: ILayer, union: bool = True) -> IPolygonSet

::
    
    def rotated(self: ~_Self, *, degrees: Optional[float] = None, radians: Optional[float] = None,
                         origin: Optional[Tuple[float, float]] = None, inplace: Optional[bool] = None) -> ~_Self
                
**Inherited from:** TransformMixin.rotated

Return a new cell reference rotated, either degrees or radians must be provided.
If both provided, radians is used …

::
    
    def run(self, processor: IProcessor)

::
    
    def scaled(self: ~_Self, sx: float, sy: Optional[float] = None, *,
                         center: Tuple[float, float] = (0, 0)) -> ~_Self
                
**Inherited from:** TransformMixin.scaled

scaled at center.

::
    
    def transform_combined(self, transform: Affine2D)
                
Return a new cell reference with a new transform which is its transform combined with the given transform.

::

     def translated(self: ~_Self, tx: float, ty: float) -> ~_Self
                
**Inherited from:** TransformMixin.translated

Translated.

::
    
    def updated(self: ~_Self, **kwargs: Any) -> ~_Self

::
    
    def v_mirrored(self: ~_Self, *, y: float = 0) -> ~_Self

**Inherited from:** TransformMixin.v_mirrored

Vertical mirrored.

::
    
    def with_bands(self: ~_Self, bands: Optional[Iterable[IBand]]) -> ~_Self
                
**Inherited from:** ICellRef.with_bands

If a class derived from ICellRef does not implement this method, it cannot be instantiated.
If a derived class of ICellRef implements this method, …

::
    
    def with_name(self: ~_Self, name: str) -> ~_Self
                
**Inherited from:** ICellRef.with_name

If a class derived from ICellRef does not implement this method, it cannot be instantiated.
If a derived class of ICellRef implements this method, …

::
    
    def with_patches(self: ~_Self, content: Iterable[IElement]) -> ~_Self
                
**Inherited from:** ICellRef.with_patches

If a class derived from ICellRef does not implement this method, it cannot be instantiated.
If a derived class of ICellRef implements this method, …

::
    
    def with_ports(self: ~_Self, ports: Sequence[Union[None, str, Hidden]]) -> ~_Self
                
**Inherited from:** ICellRef.with_ports
                    
If a class derived from ICellRef does not implement this method, it cannot be instantiated.
If a derived class of ICellRef implements this method, …