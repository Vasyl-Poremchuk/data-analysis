import numpy as np


def convert_list(list_numbers: list[int]) -> np.ndarray | ValueError:
    """
    The function checks whether the input list contains 9 numbers and
    returns a 3x3 matrix. On the other hand, it throws a `ValueError`
    exception.
    """
    if len(list_numbers) == 9:
        array_numbers = np.array(list_numbers).reshape(3, 3)

        return array_numbers

    raise ValueError("List must contain nine numbers.")


def get_mean(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `mean` value along both axes
    and for the flattened matrix.
    """
    col_mean = np.mean(array_numbers, axis=0).tolist()
    row_mean = np.mean(array_numbers, axis=1).tolist()
    flattened_mean = np.mean(array_numbers).tolist()

    return {"mean": [col_mean, row_mean, flattened_mean]}


def get_variance(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `variance` value along both axes
    and for the flattened matrix.
    """
    col_variance = np.var(array_numbers, axis=0).tolist()
    row_variance = np.var(array_numbers, axis=1).tolist()
    flattened_variance = np.var(array_numbers).tolist()

    return {"variance": [col_variance, row_variance, flattened_variance]}


def get_standard_deviation(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `standard_deviation` value along both axes
    and for the flattened matrix.
    """
    col_standard_deviation = np.std(array_numbers, axis=0).tolist()
    row_standard_deviation = np.std(array_numbers, axis=1).tolist()
    flattened_standard_deviation = np.std(array_numbers).tolist()

    return {
        "standard_deviation": [
            col_standard_deviation,
            row_standard_deviation,
            flattened_standard_deviation,
        ]
    }


def get_max(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `max` value along both axes
    and for the flattened matrix.
    """
    col_max = np.max(array_numbers, axis=0).tolist()
    row_max = np.max(array_numbers, axis=1).tolist()
    flattened_variance_max = np.max(array_numbers).tolist()

    return {"max": [col_max, row_max, flattened_variance_max]}


def get_min(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `min` value along both axes
    and for the flattened matrix.
    """
    col_min = np.min(array_numbers, axis=0).tolist()
    row_min = np.min(array_numbers, axis=1).tolist()
    flattened_min = np.min(array_numbers).tolist()

    return {"min": [col_min, row_min, flattened_min]}


def get_sum(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns the `sum` value along both axes
    and for the flattened matrix.
    """
    col_sum = np.sum(array_numbers, axis=0).tolist()
    row_sum = np.sum(array_numbers, axis=1).tolist()
    flattened_sum = np.sum(array_numbers).tolist()

    return {"sum": [col_sum, row_sum, flattened_sum]}


def calculate(array_numbers: np.ndarray) -> dict[str, list]:
    """
    The function returns a dictionary containing the names of the measures
    as key, and their corresponding values as values.
    """
    result = (
        get_mean(array_numbers)
        | get_variance(array_numbers)
        | get_standard_deviation(array_numbers)
        | get_max(array_numbers)
        | get_max(array_numbers)
        | get_min(array_numbers)
        | get_sum(array_numbers)
    )

    return result
