from matrix import Matrix3x3, Matrix2x2
from pytest import fixture


@fixture
def matrix_3x3() -> Matrix3x3:
    return Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])


@fixture
def matrix_2x2() -> Matrix2x2:
    return Matrix2x2.from_iterable([1.0, 2.0, 3.0, 4.0])
