Module fnpcell.transform
=============================

Affine2D transformations

Functions
------------

c_mirror
+++++++++

::
    
    def c_mirror(*, center: Tuple[float, float] = (0, 0)) -> Affine2D

Center mirror.

h_mirror
++++++++++

::
    
    def h_mirror(*, x: float = 0) -> Affine2D

Horizontal mirror.

rotate
+++++++++

::
    
    def rotate(*, degrees: Optional[float] = None, radians: Optional[float] = None, 
                center: Tuple[float, float] = (0, 0)) -> Affine2D

Rotated at center anticlockwise.

scale
++++++

::
    
    def scale(sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> Affine2D

Scale at center.

translate
+++++++++++

::
    
    def translate(tx: float, ty: float) -> Affine2D

Translate.

v_mirror
++++++++++

::
    
    def v_mirror(*, y: float = 0) -> Affine2D

Vertical mirror.

Classes
----------

Affine2D
++++++++++

::
    
    class Affine2D(11: float = 1, m12: float = 0, m21: float = 0, 
                    m22: float = 1, m31: float = 0, m32: float = 0)

Affine2D transformation matrix.

Usage::
    
    from fnpcell import all as fp

    t = fp.translate(10, 0)
    r = fp.rotate(degrees=30)
    transform = t @ r

    assert transform == fp.translate(10, 0).rotate(degrees=30)

    points = [(0, 0), (1, 0), (1, 1)]
    transformed_points = transform(points)  # equals to transform.transform_points(points)

Class variables
_________________

::
    
    var m11: float
    var m12: float
    var m21: float
    var m22: float
    var m31: float
    var m32: float

Static methods
_________________

::
    
    def identity() -> Affine2D

Returns the identity matrix of Affine2D.

::
    
    def is_identity(value: Affine2D) -> bool

Determine whether the transform is equal to the identity matrix.

::
    
    def is_nonidentity(value: Affine2D) -> bool

Determine whether the transform is not equal to the identity matrix.

::
    
    def is_safe_transform(transform: Affine2D, grid: float) -> bool

Determine whether a transform can avoid causing off-grid, 
which means making sure all points are on the grid.

::
    
    def new(scaling: Tuple[float, float], rotation: float, 
            translation: Tuple[float, float]) -> Affine2D

Instance variables
____________________

::
    
    var translation : Tuple[float, float]

Methods
________

::
    
    def c_mirror(self, *, center: Tuple[float, float] = (0, 0)) -> Affine2D

Returns the center mirrored transform.

::
    
    def decompose(self) -> Tuple[Tuple[float, float], float, Tuple[float, float]]

Returns scaling, rotation, translation for transform.

::
    
    def determinant(self) -> float

The determinant is the ratio used to express the scaling of space. 
When the determinant is 0, it means that there is no inverse matrix. 
When the determinant is not 0, it means that an inverse matrix exists.

::
    
    def h_mirror(self, *, x: float = 0) -> Affine2D

Returns the horizontal mirrored transform.

::
    
    def inverse(self) -> Affine2D

Returns an inverse matrix transformation that represents the inverse of the Affine2D transform, 
which is used to restore the original image before the transformation. When the determinant is 0, 
the inverse matrix transformation does not exist and an identity matrix is returned.

::
    
    def rotate(self, *, degrees: Optional[float] = None, radians: Optional[float] = None, 
                center: Tuple[float, float] = (0, 0)) -> Affine2D

Create a rotation transform at the specified angle or degree.

::
    
    def scale(self, sx: float, sy: Optional[float] = None, *, 
                center: Tuple[float, float] = (0, 0)) -> Affine2D

Around the center point, returns a scaling transform based on the x-axis scaling and the y-axis scaling.

::
    
    def transform_angle(self, angle: float) -> float

::
    
    def transform_point(self, point: Tuple[float, float]) -> Tuple[float, float]

::
    
    def transform_points(self, points: Iterable[Tuple[float, float]]) -> Tuple[Tuple[float, float], ...]

::
    
    def translate(self, tx: float, ty: float) -> Affine2D

Returns the translated transform.

::
    
    def v_mirror(self, *, y: float = 0) -> Affine2D
    
Returns the vertical mirrored transform.