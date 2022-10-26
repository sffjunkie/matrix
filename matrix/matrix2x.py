import collections.abc
from numbers import Number

from typing_extensions import Self

from matrix.base import Matrix


class Matrix2x1(Matrix):
    def __init__(self, data: list[Number] | None = None):
        if data is None:
            self.data = [0.0, 0.0]
        else:
            self.data = data[:2]

    def __getitem__(self, idx):
        return self.data[idx]

    def __mul__(self, other: Number):
        data = [self.data[0] * other, self.data[1] * other]
        return Matrix2x1.from_iterable(data)

    @classmethod
    def from_iterable(cls, number_array: collections.abc.Iterable[Number]):
        return cls(number_array)


class Matrix2x2(Matrix):
    def __init__(self, data: list[Number] | None = None):
        if data is None:
            self.data = [[0.0] * 2] * 2
        else:
            self.data = data[:2]

    def __getitem__(self, idx):
        return self.data[idx]

    def __mul__(self, other: Matrix | Number) -> Self:
        if isinstance(other, Matrix2x2):
            return matrix_multiply_2x2(self, other)
        elif isinstance(other, Matrix2x1):
            return matrix_multiply_2x1(self, other)
        elif isinstance(other, Number):
            d = self.data
            data = [
                d[0][0] * other,
                d[0][1] * other,
                d[1][0] * other,
                d[1][1] * other,
            ]
            return Matrix2x2.from_iterable(data)

    @classmethod
    def from_iterable(cls, number_array: collections.abc.Iterable[Number]):
        if isinstance(number_array[0], list):
            return cls(number_array)
        return cls([number_array[:2], number_array[2:4]])

    def transpose(self) -> Self:
        d = self.data[:]
        d[0][1], d[1][0] = d[1][0], d[0][1]
        return Matrix2x2.from_iterable(d)

    def determinant(self) -> Number:
        return (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])

    def inverse(self) -> Self:
        if self.determinant == 0:
            raise ValueError("Determinant is 0: Unable to calculate inverse")

        d = self.data[:]
        d[0][0], d[1][1] = d[1][1], d[0][0]
        d[0][1] = -d[0][1]
        d[1][0] = -d[1][0]

        data = [item for sublist in d for item in sublist]
        m = Matrix2x2.from_iterable(data)

        det = self.determinant()
        return m * (1 / det)


def matrix_multiply_2x1(a: Matrix2x2, b: Matrix2x1) -> Matrix2x1:
    return Matrix2x1.from_iterable(
        (a[0][0] * b[0] + a[0][1] * b[1], a[1][0] * b[0] + a[1][1] * b[1])
    )


def matrix_multiply_2x2(a: Matrix2x2, b: Matrix2x2) -> Matrix2x2:
    elems = (
        (a[0][0] * b[0][0] + a[0][1] * b[0][1], a[0][0] * b[1][0] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[0][1], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )
    return Matrix2x2.from_iterable(elems)
