from pytest import fixture

from matrix import Matrix2x2, Matrix3x3


@fixture
def matrix_3x3() -> Matrix3x3:
    return Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])


@fixture
def matrix_3x3_1() -> Matrix3x3:
    return Matrix3x3.from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])


@fixture
def matrix_2x2() -> Matrix2x2:
    return Matrix2x2.from_iterable([1.0, 2.0, 3.0, 4.0])
