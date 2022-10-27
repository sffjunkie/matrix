import pytest

from matrix import Matrix2x2


def test_2x2_empty():
    m = Matrix2x2()
    assert m.data == ((1.0, 0.0), (0.0, 1.0))


def test_2x2_from_iterable_float():
    data = (1.0, 2.0, 3.0, 4.0)

    m = Matrix2x2.from_iterable(data)

    assert m[0][0] == 1.0
    assert m[1][1] == 4.0


def test_2x2_from_iterable_iterable():
    data = ((1.0, 2.0), (3.0, 4.0))

    m = Matrix2x2.from_iterable(data)

    assert m[0][0] == 1.0
    assert m[1][1] == 4.0


def test_2x2_determinant(matrix_2x2):
    det = matrix_2x2.determinant()

    assert det == -2


def test_2x2_transpose(matrix_2x2):
    m = matrix_2x2.transpose()

    assert m.data == ((1, 3), (2, 4))


def test_2x2_inverse(matrix_2x2):
    m = matrix_2x2.inverse()

    assert m.data == ((-2.0, 1.0), (1.5, -0.5))


def test_multiply_2x2_2x2(matrix_2x2):
    m = matrix_2x2 * matrix_2x2

    assert isinstance(m, Matrix2x2)
    assert m.data == ((7.0, 10.0), (15.0, 22.0))


def test_multiply_2x2_2x1(matrix_2x2, matrix_2x1):
    m = matrix_2x2 * matrix_2x1
    assert m.data == (5, 11)


def test_multiply_2x2_scalar(matrix_2x2):
    n = matrix_2x2 * 2.5

    assert isinstance(n, Matrix2x2)
    assert n[0][0] == 2.5
    assert n[1][1] == 10


def test_equals_2x2(matrix_2x2):
    assert matrix_2x2 == matrix_2x2


def test_equals_2x2_bad(matrix_2x2):
    with pytest.raises(TypeError):
        matrix_2x2 == 1


def test_inverse_2x2_determinent_0_fails():
    data = (1.0, 1.0, 2.0, 2.0)
    with pytest.raises(ValueError):
        Matrix2x2.from_iterable(data).inverse()


def test_identity_2x2():
    m = Matrix2x2.identity()
    assert m.data == ((1.0, 0.0), (0.0, 1.0))
