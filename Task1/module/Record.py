from nameof import nameof

from module.util import to_string_class_formatter


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
