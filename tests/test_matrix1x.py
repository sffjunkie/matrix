from numbers import Number

import pytest

from matrix import Matrix1x2, Matrix1x3, Matrix3x1


def test_1x2_empty():
    m = Matrix1x2()

    assert m[0] == 0.0
    assert m[1] == 0.0


def test_1x2_repr():
    r = repr(Matrix1x2())
    assert r == "Matrix1x2 = (0.0, 0.0)"


def test_1x2_from_list():
    data = [1.0, 2.0]

    m = Matrix1x2.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0


def test_1x2_from_tuple():
    data = (1.0, 2.0)

    m = Matrix1x2.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0


def test_multiply_1x2_scalar(matrix_1x2):
    n = matrix_1x2 * 2.5

    assert isinstance(n, Matrix1x2)
    assert n[0] == 2.5
    assert n[1] == 5


def test_multiply_1x2_2x1(matrix_2x1, matrix_1x2):
    n = matrix_1x2 * matrix_2x1

    assert isinstance(n, Number)
    assert n == 5.0


def test_multiply_1x2_bad(matrix_2x2, matrix_1x2):
    with pytest.raises(TypeError):
        matrix_1x2 * matrix_2x2


def test_1x2_equals(matrix_1x2):
    data = (1.0, 2.0)
    m = Matrix1x2.from_iterable(data)

    assert m == matrix_1x2


def test_1x2_equals_bad_type(matrix_1x2):
    with pytest.raises(TypeError):
        matrix_1x2 == 1


def test_1x3_empty():
    m = Matrix1x3()

    assert m[0] == 0.0
    assert m[1] == 0.0
    assert m[2] == 0.0


def test_1x3_repr():
    r = repr(Matrix1x3())
    assert r == "Matrix1x3 = (0.0, 0.0, 0.0)"


def test_1x3_from_list():
    data = [1.0, 2.0, 3.0]

    m = Matrix1x3.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0
    assert m[2] == 3.0


def test_1x3_from_tuple():
    data = (1.0, 2.0, 3.0)

    m = Matrix1x3.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0
    assert m[2] == 3.0


def test_1x3_multiply_scalar(matrix_1x3):
    n = matrix_1x3 * 2.5

    assert isinstance(n, Matrix1x3)
    assert n[0] == 2.5
    assert n[1] == 5


def test_1x3_equals(matrix_1x3):
    data = (1.0, 2.0, 3.0)
    m = Matrix1x3.from_iterable(data)

    assert m == matrix_1x3


def test_1x3_equals_bad_type(matrix_1x3):
    with pytest.raises(TypeError):
        matrix_1x3 == 1


def test_multiply_1x3_3x1(matrix_3x1: Matrix3x1, matrix_1x3: Matrix1x3):
    n = matrix_1x3 * matrix_3x1

    assert isinstance(n, Number)
    assert n == 14


def test_multiply_1x3_bad(matrix_2x2, matrix_1x3):
    with pytest.raises(TypeError):
        matrix_1x3 * matrix_2x2
