from typing import List


def to_string_class_formatter(variables: List[object], variables_names: List[str],
                              separator: str = "\t") -> str:
    if len(variables) != len(variables):
        raise Exception("Both arrays must have equal size")

    result: str = ""
    for i in range(len(variables)):
        result += variables_names[i] + ": " + str(variables[i]) + separator

    return result


def is_convertible_to_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_convertible_to_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_array_convertible_to_int(value: List[str]) -> bool:
    try:
        [int(item) for item in value]
        return True
    except ValueError:
        return False
