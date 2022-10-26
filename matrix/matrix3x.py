import collections.abc
from numbers import Number

from typing_extensions import Self

from matrix.base import Matrix
from matrix.matrix2x import Matrix2x2


class Matrix3x1(Matrix):
    def __init__(self, data: list[Number] | None = None):
        if data is None:
            self.data = [0.0, 0.0, 0.0]
        else:
            self.data = data[:3]

    def __getitem__(self, idx):
        return self.data[idx]

    def __mul__(self, other: Number):
        d = self.data
        data = [d[0] * other, d[1] * other, d[2] * other]
        return Matrix3x1.from_iterable(data)

    @classmethod
    def from_iterable(cls, number_array: collections.abc.Iterable[Number]):
        return cls(number_array[:3])


class Matrix3x3(Matrix):
    def __init__(self, data: list[list[Number]] | None = None):
        if data is None:
            self.data = [[0.0] * 3] * 3
        else:
            self.data = data

    def __getitem__(self, idx):
        return self.data[idx]

    def __mul__(self, other: Matrix | Number) -> Self:
        if isinstance(other, Matrix3x3):
            return matrix_multiply_3x3(self, other)
        elif isinstance(other, Matrix3x1):
            return matrix_multiply_3x1(self, other)
        elif isinstance(other, Number):
            data = []
            for row in range(3):
                for column in range(3):
                    data.append(self.data[row][column] * other)

            return Matrix3x3.from_iterable(data)

    @classmethod
    def from_iterable(cls, number_array: collections.abc.Iterable[Number]):
        if isinstance(number_array[0], list):
            return cls(number_array)
        return cls([number_array[:3], number_array[3:6], number_array[6:9]])

    def transpose(self) -> Self:
        d = self.data[:]
        d[1][0], d[0][1] = d[0][1], d[1][0]
        d[2][0], d[0][2] = d[0][2], d[2][0]
        d[2][1], d[1][2] = d[2][1], d[1][2]
        data = [item for sublist in d for item in sublist]
        return Matrix3x3.from_iterable(data)

    def determinant(self) -> Number:
        d = [self.data[0] * 2, self.data[1] * 2, self.data[2] * 2]
        return (
            d[0][0] * d[1][1] * d[2][2]
            + d[0][1] * d[1][2] * d[2][3]
            + d[0][2] * d[1][3] * d[2][4]
            - d[0][0] * d[1][2] * d[2][1]
            - d[0][1] * d[1][0] * d[2][2]
            - d[0][2] * d[1][1] * d[2][0]
        )

    def adjoint(self) -> Self:
        elements: list[list[Matrix2x2]] = [[], [], []]

        d = self.data
        all_rows = set(range(3))
        all_columns = set(range(3))
        for row in range(3):
            other_rows = tuple(all_rows - set((row,)))
            for column in range(3):
                other_columns = tuple(all_columns - set((column,)))
                tl = d[other_rows[0]][other_columns[0]]
                bl = d[other_rows[1]][other_columns[0]]
                tr = d[other_rows[0]][other_columns[1]]
                br = d[other_rows[1]][other_columns[1]]
                m = Matrix2x2.from_iterable([tl, tr, bl, br])
                elements[row].append(m)

        sign = 1
        dets = []
        for row in range(3):
            for column in range(3):
                dets.append(elements[row][column].determinant() * sign)
                sign *= -1

        m = Matrix3x3.from_iterable(dets)
        return m.transpose()

    def inverse(self) -> Self:
        adjoint = self.adjoint()
        determinant = self.determinant()
        return adjoint * (1 / determinant)


def matrix_multiply_3x1(a: Matrix3x3, b: Matrix3x1) -> Matrix3x1:
    elems = (
        b[0] * a[0][0] + b[1] * a[0][1] + b[2] * a[0][2],
        b[0] * a[1][0] + b[1] * a[1][1] + b[2] * a[1][2],
        b[0] * a[2][0] + b[1] * a[2][1] + b[2] * a[2][2],
    )
    return Matrix3x1.from_iterable(elems)


def matrix_multiply_3x3(a: Matrix3x3, b: Matrix3x3) -> Matrix3x3:
    """3x3 matrix multiplication

    http://www.ams.org/journals/bull/1976-82-01/S0002-9904-1976-13988-2/S0002-9904-1976-13988-2.pdf
    """
    terms = []

    terms[1] = (
        a[0][0] + a[0][1] + a[0][2] - a[1][0] - a[1][1] - a[2][1] - a[2][2]
    ) * b[1][1]
    terms[2] = (a[0][0] - a[1][0]) * (-b[0][1] + b[1][1])
    terms[3] = a[1][1] * (
        -b[0][0] + b[0][1] + b[1][0] - b[1][1] - b[1][2] - b[2][0] + b[2][2]
    )
    terms[4] = (-a[0][0] + a[1][0] + a[1][1]) * (b[0][0] - b[0][1] + b[1][1])
    terms[5] = (a[1][0] + a[1][1]) * (-b[0][0] + b[0][1])
    terms[6] = a[0][0] * b[0][0]
    terms[7] = (-a[0][0] + a[2][0] + a[2][1]) * (b[0][0] - b[0][2] + b[1][2])
    terms[8] = (-a[0][0] + a[2][0]) * (b[0][2] - b[1][2])
    terms[9] = (a[2][0] + a[2][1]) * (-b[0][0] + b[0][2])
    terms[10] = (
        a[0][0] + a[0][1] + a[0][2] - a[1][1] - a[1][2] - a[2][0] - a[2][1]
    ) * b[1][2]
    terms[11] = a[2][1] * (
        -b[0][0] + b[0][2] + b[1][0] - b[1][1] - b[1][2] - b[2][0] + b[2][1]
    )
    terms[12] = (-a[0][2] + a[2][1] + a[2][2]) * (b[1][1] + b[2][0] - b[2][1])
    terms[13] = (a[0][2] - a[2][2]) * (b[1][1] - b[2][1])
    terms[14] = a[0][2] * b[2][0]
    terms[15] = (a[2][1] + a[2][2]) * (-b[2][0] + b[2][1])
    terms[16] = (-a[0][2] + a[1][1] + a[1][2]) * (b[1][2] + b[2][0] - b[2][2])
    terms[17] = (a[0][2] - a[1][2]) * (b[1][2] - b[2][2])
    terms[18] = (a[1][1] + a[1][2]) * (-b[2][0] + b[2][2])
    terms[19] = a[0][1] * b[1][0]
    terms[20] = a[1][2] * b[2][1]
    terms[21] = a[1][0] * b[0][2]
    terms[22] = a[2][0] * b[0][1]
    terms[23] = a[2][2] * b[2][2]

    return Matrix3x3.from_iterable(
        [
            terms[6] + terms[14] + terms[19],
            terms[1]
            + terms[4]
            + terms[5]
            + terms[6]
            + terms[12]
            + terms[14]
            + terms[15],
            terms[6]
            + terms[7]
            + terms[9]
            + terms[10]
            + terms[14]
            + terms[16]
            + terms[18],
            terms[2]
            + terms[3]
            + terms[4]
            + terms[6]
            + terms[14]
            + terms[16]
            + terms[17],
            terms[2] + terms[4] + terms[5] + terms[6] + terms[20],
            terms[14] + terms[16] + terms[17] + terms[18] + terms[21],
            terms[6]
            + terms[7]
            + terms[8]
            + terms[11]
            + terms[12]
            + terms[13]
            + terms[14],
            terms[12] + terms[13] + terms[14] + terms[15] + terms[22],
            terms[6] + terms[7] + terms[8] + terms[9] + terms[23],
        ]
    )
