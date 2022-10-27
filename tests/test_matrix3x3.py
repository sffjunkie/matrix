import pytest

from matrix import Matrix3x1, Matrix3x3


def test_3x3_empty():
    m = Matrix3x3()
    assert m.data == ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))


def test_3x3_repr():
    r = repr(Matrix3x3())
    assert r == "Matrix3x3 = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"


def test_3x3_rich_repr():
    r = tuple(Matrix3x3().__rich_repr__())
    assert r == (
        "Matrix3x3",
        ("data", ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))),
    )


def test_3x3_from_iterable():
    m = Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])
    assert m[1][1] == 1
    assert m[2][2] == 1


def test_3x3_determinant(matrix_3x3: Matrix3x3):
    det = matrix_3x3.determinant()
    assert det == -16


def test_3x3_adjoint(matrix_3x3):
    adjoint = matrix_3x3.adjoint()
    assert adjoint[0][1] == -4


def test_3x3_inverse(matrix_3x3):
    inverse = matrix_3x3.inverse()
    assert inverse[0][0] == pytest.approx(3.0 / 16.0)


def test_3x3_transpose(matrix_3x3_1):
    m = matrix_3x3_1.transpose()
    assert m.data == (
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
    )


def test_multiply_3x3_3x3():
    m1 = Matrix3x3.from_iterable(((2, 3, 1), (7, 4, 1), (9, -2, 1)))
    m2 = Matrix3x3.from_iterable(((9, -2, -1), (5, 7, 3), (8, 1, 0)))
    m = m1 * m2

    ans = Matrix3x3.from_iterable(((41, 18, 7), (91, 15, 5), (79, -31, -15)))

    assert ans == m


def test_multiply_3x3_1x3(matrix_3x3, matrix_3x1):
    n = matrix_3x3 * matrix_3x1

    assert isinstance(n, Matrix3x1)
    assert n.data == (2.0, 10.0, 6.0)


def test_multiply_3x3_scalar(matrix_3x3):
    n = matrix_3x3 * 3

    assert isinstance(n, Matrix3x3)

    assert n.data == ((3.0, 6.0, -3.0), (6.0, 3.0, 6.0), (-3.0, 6.0, 3.0))


def test_multiply_3x3_bad(matrix_3x3, matrix_2x2):
    with pytest.raises(TypeError):
        matrix_3x3 * matrix_2x2


def test_3x3_inverse_determinant_0():
    data = (1, 2, 3, 0, 2, 2, 1, 4, 5)

    m = Matrix3x3.from_iterable(data)

    with pytest.raises(ValueError):
        m.inverse()


def test_identity_3x3():
    m = Matrix3x3.identity()
    assert m.data == ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))


def test_equals_3x3(matrix_3x3):
    assert matrix_3x3 == Matrix3x3.from_iterable([1, 2, -1, 2, 1, 2, -1, 2, 1])


def test_equals_3x3_bad(matrix_3x3, matrix_3x1):
    with pytest.raises(TypeError):
        matrix_3x3 == 1

    with pytest.raises(TypeError):
        matrix_3x3 == matrix_3x1
