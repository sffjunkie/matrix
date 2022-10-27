from typing import Any


class Matrix:
    def __eq__(self, other: Any):
        if isinstance(other, self.__class__):
            return self.data == other.data
        else:
            raise TypeError(
                f"Unable to compare {self.__class__.__name__} to {type(other)}"
            )
