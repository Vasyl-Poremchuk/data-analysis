import numpy as np
import pytest

from mean_variance_standard_deviation_calculator.mean_var_std import (
    convert_list,
    get_mean,
    get_variance,
    get_standard_deviation,
    get_max,
    get_min,
    get_sum,
    calculate,
)


@pytest.mark.parametrize(
    "input_list,expected_output",
    [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ),
        (
            [10, 11, 12, 13, 14, 15, 16, 17, 18],
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
        ),
        ([19, 20, 21, 22, 23, 24, 25, 26], ValueError),
        ([27, 28, 29, 30, 31, 32, 33, 34, 35, 36], ValueError),
        ([], ValueError),
    ],
)
def test_convert_list(
    input_list: list[int], expected_output: np.ndarray | ValueError
) -> None:
    if isinstance(expected_output, np.ndarray):
        assert (convert_list(input_list) == expected_output).all()
    else:
        with pytest.raises(
            expected_output, match="List must contain nine numbers."
        ):
            convert_list(input_list)


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {"mean": [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0]},
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {"mean": [[13.0, 14.0, 15.0], [11.0, 14.0, 17.0], 14.0]},
        ),
    ],
)
def test_get_mean(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_mean(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {
                "variance": [
                    [6.0, 6.0, 6.0],
                    [
                        0.6666666666666666,
                        0.6666666666666666,
                        0.6666666666666666,
                    ],
                    6.666666666666667,
                ]
            },
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {
                "variance": [
                    [6.0, 6.0, 6.0],
                    [
                        0.6666666666666666,
                        0.6666666666666666,
                        0.6666666666666666,
                    ],
                    6.666666666666667,
                ]
            },
        ),
    ],
)
def test_get_variance(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_variance(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {
                "standard_deviation": [
                    [2.449489742783178, 2.449489742783178, 2.449489742783178],
                    [0.816496580927726, 0.816496580927726, 0.816496580927726],
                    2.581988897471611,
                ]
            },
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {
                "standard_deviation": [
                    [2.449489742783178, 2.449489742783178, 2.449489742783178],
                    [0.816496580927726, 0.816496580927726, 0.816496580927726],
                    2.581988897471611,
                ]
            },
        ),
    ],
)
def test_get_standard_deviation(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_standard_deviation(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {"max": [[7, 8, 9], [3, 6, 9], 9]},
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {"max": [[16, 17, 18], [12, 15, 18], 18]},
        ),
    ],
)
def test_get_max(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_max(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {"min": [[1, 2, 3], [1, 4, 7], 1]},
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {"min": [[10, 11, 12], [10, 13, 16], 10]},
        ),
    ],
)
def test_get_min(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_min(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {"sum": [[12, 15, 18], [6, 15, 24], 45]},
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {"sum": [[39, 42, 45], [33, 42, 51], 126]},
        ),
    ],
)
def test_get_sum(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert get_sum(input_array) == expected_output


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            {
                "mean": [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
                "variance": [
                    [6.0, 6.0, 6.0],
                    [
                        0.6666666666666666,
                        0.6666666666666666,
                        0.6666666666666666,
                    ],
                    6.666666666666667,
                ],
                "standard_deviation": [
                    [2.449489742783178, 2.449489742783178, 2.449489742783178],
                    [0.816496580927726, 0.816496580927726, 0.816496580927726],
                    2.581988897471611,
                ],
                "max": [[7, 8, 9], [3, 6, 9], 9],
                "min": [[1, 2, 3], [1, 4, 7], 1],
                "sum": [[12, 15, 18], [6, 15, 24], 45],
            },
        ),
        (
            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
            {
                "mean": [[13.0, 14.0, 15.0], [11.0, 14.0, 17.0], 14.0],
                "variance": [
                    [6.0, 6.0, 6.0],
                    [
                        0.6666666666666666,
                        0.6666666666666666,
                        0.6666666666666666,
                    ],
                    6.666666666666667,
                ],
                "standard_deviation": [
                    [2.449489742783178, 2.449489742783178, 2.449489742783178],
                    [0.816496580927726, 0.816496580927726, 0.816496580927726],
                    2.581988897471611,
                ],
                "max": [[16, 17, 18], [12, 15, 18], 18],
                "min": [[10, 11, 12], [10, 13, 16], 10],
                "sum": [[39, 42, 45], [33, 42, 51], 126],
            },
        ),
    ],
)
def test_calculate(
    input_array: np.ndarray, expected_output: dict[str, list]
) -> None:
    assert calculate(input_array) == expected_output
