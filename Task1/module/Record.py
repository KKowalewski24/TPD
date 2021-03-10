from typing import List

from nameof import nameof


class Record:

    def __init__(self, row_number: int, value: float) -> None:
        self.row_number = row_number
        self.value = value

    def __str__(self) -> str:
        return to_string_class_formatter(
            [self.row_number, self.value],
            [nameof(self.row_number), nameof(self.value), ],
            "\t\t"
        )


def to_string_class_formatter(variables: List[object], variables_names: List[str],
                              separator: str = "\t") -> str:
    if len(variables) != len(variables):
        raise Exception("Both arrays must have equal size")

    result: str = ""
    for i in range(len(variables)):
        result += variables_names[i] + ": " + str(variables[i]) + separator

    return result
