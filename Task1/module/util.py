from typing import List


def to_string_class_formatter(variables: List[object], variables_names: List[str],
                              separator: str = "\t") -> str:
    if len(variables) != len(variables):
        raise Exception("Both arrays must have equal size")

    result: str = ""
    for i in range(len(variables)):
        result += variables_names[i] + ": " + str(variables[i]) + separator

    return result
