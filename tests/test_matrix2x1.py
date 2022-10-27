import pytest

from matrix import Matrix2x1


def test_2x1_empty():
    m = Matrix2x1()

    assert m[0] == 0.0
    assert m[1] == 0.0


def test_2x1_repr():
    r = repr(Matrix2x1())
    assert r == "Matrix2x1 = (0.0, 0.0)"


def test_2x1_from_list():
    data = [1.0, 2.0]

    m = Matrix2x1.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0


def test_2x1_from_tuple():
    data = (1.0, 2.0)

    m = Matrix2x1.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0


def test_multiply_2x1_scalar(matrix_2x1):
    n = matrix_2x1 * 2.5

    assert isinstance(n, Matrix2x1)
    assert n[0] == 2.5
    assert n[1] == 5


def test_multiply_2x1_bad(matrix_2x1, matrix_3x3):
    with pytest.raises(TypeError):
        matrix_2x1 * matrix_3x3


def test_2x1_equals(matrix_2x1):
    data = (1.0, 2.0)
    m = Matrix2x1.from_iterable(data)

    assert m == matrix_2x1


def test_2x1_equals_bad_type(matrix_2x1):
    with pytest.raises(TypeError):
        matrix_2x1 == 1
