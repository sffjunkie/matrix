from pytest import fixture

from matrix.matrix1x import Matrix1x2, Matrix1x3
from matrix.matrix2x import Matrix2x1, Matrix2x2
from matrix.matrix3x import Matrix3x1, Matrix3x3


@fixture
def matrix_1x2() -> Matrix1x2:
    return Matrix1x2.from_iterable([1.0, 2.0])


@fixture
def matrix_1x3() -> Matrix1x3:
    return Matrix1x3.from_iterable([1.0, 2.0, 3.0])


@fixture
def matrix_2x1() -> Matrix2x1:
    return Matrix2x1.from_iterable([1, 2])


@fixture
def matrix_2x2() -> Matrix2x2:
    return Matrix2x2.from_iterable([1.0, 2.0, 3.0, 4.0])


@fixture
def matrix_2x2_1() -> Matrix2x2:
    return Matrix2x2.from_iterable([1.0, 2.0, 3.0, 4.0])


@fixture
def matrix_3x1() -> Matrix3x1:
    return Matrix3x1.from_iterable([1, 2, 3])


@fixture
def matrix_3x3() -> Matrix3x3:
    return Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])


@fixture
def matrix_3x3_1() -> Matrix3x3:
    return Matrix3x3.from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
