from matrix import Matrix2x2


def test_matrix2x2_from_iterable_float():
    data = [1.0, 2.0, 3.0, 4.0]

    m = Matrix2x2.from_iterable(data)

    assert m[0][0] == 1.0
    assert m[1][1] == 4.0


def test_matrix2x2_from_iterable_list():
    data = [[1.0, 2.0], [3.0, 4.0]]

    m = Matrix2x2.from_iterable(data)

    assert m[0][0] == 1.0
    assert m[1][1] == 4.0


def test_matrix2x2_multiply(matrix_2x2):
    n = matrix_2x2 * 2.5

    assert isinstance(n, Matrix2x2)
    assert n[0][0] == 2.5
    assert n[1][1] == 10


def test_matrix2x2_determinant(matrix_2x2):
    det = matrix_2x2.determinant()

    assert det == -2
