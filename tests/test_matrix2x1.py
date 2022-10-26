from matrix import Matrix2x1


def test_matrix2x1_from_iterable():
    data = [1.0, 2.0]

    m = Matrix2x1.from_iterable(data)

    assert m[0] == 1.0
    assert m[1] == 2.0


def test_matrix2x1_multiply():
    data = [1.0, 2.0]
    m = Matrix2x1.from_iterable(data)

    n = m * 2.5

    assert isinstance(n, Matrix2x1)
    assert n[0] == 2.5
    assert n[1] == 5
