import pytest
from matrix import Matrix3x3


def test_matrix3x3_from_iterable():
    m = Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])
    assert m[1][1] == 1
    assert m[2][2] == 1


def test_matrix3x3_determinant(matrix_3x3: Matrix3x3):
    det = matrix_3x3.determinant()
    assert det == -16


def test_matrix3x3_adjoint(matrix_3x3):
    adjoint = matrix_3x3.adjoint()
    assert adjoint[0][1] == -4


def test_matrix3x3_inverse(matrix_3x3):
    inverse = matrix_3x3.inverse()
    assert inverse[0][0] == pytest.approx(3.0 / 16.0)
