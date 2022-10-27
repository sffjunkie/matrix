import pytest

from matrix.matrix3x import Matrix3x1


def test_matrix3x1_empty():
    m = Matrix3x1()

    assert m[0] == 0.0
    assert m[1] == 0.0
    assert m[2] == 0.0


def test_3x1_repr():
    r = repr(Matrix3x1())
    assert r == "Matrix3x1 = (0.0, 0.0, 0.0)"


def test_matrix3x1_from_list():
    data = [1.0, 2.0, 3.0]

    m = Matrix3x1.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0
    assert m[2] == 3.0


def test_matrix3x1_from_tuple():
    data = (1.0, 2.0, 3.0)

    m = Matrix3x1.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0
    assert m[2] == 3.0


def test_multiply_3x1_scalar(matrix_3x1: Matrix3x1):
    n = matrix_3x1 * 2.5

    assert isinstance(n, Matrix3x1)
    assert n[0] == 2.5
    assert n[1] == 5
    assert n[2] == 7.5


def test_multiply_3x1_bad(matrix_3x1: Matrix3x1, matrix_2x1):
    with pytest.raises(TypeError):
        matrix_3x1 * matrix_2x1


def test_equals_3x1(matrix_3x1: Matrix3x1):
    assert matrix_3x1 == matrix_3x1


def test_equals_3x1_bad(matrix_3x1: Matrix3x1, matrix_2x1):
    with pytest.raises(TypeError):
        matrix_3x1 == matrix_2x1
