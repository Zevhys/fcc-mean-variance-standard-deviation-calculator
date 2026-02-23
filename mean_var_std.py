import numpy as np


def calculate(list_input):
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")

    array_3x3 = np.array(list_input).reshape(3, 3)

    mean_axis0 = np.mean(array_3x3, axis=0)
    mean_axis1 = np.mean(array_3x3, axis=1)
    mean_flattened = np.mean(array_3x3)

    var_axis0 = np.var(array_3x3, axis=0)
    var_axis1 = np.var(array_3x3, axis=1)
    var_flattened = np.var(array_3x3)

    std_axis0 = np.std(array_3x3, axis=0)
    std_axis1 = np.std(array_3x3, axis=1)
    std_flattened = np.std(array_3x3)

    max_axis0 = np.max(array_3x3, axis=0)
    max_axis1 = np.max(array_3x3, axis=1)
    max_flattened = np.max(array_3x3)

    min_axis0 = np.min(array_3x3, axis=0)
    min_axis1 = np.min(array_3x3, axis=1)
    min_flattened = np.min(array_3x3)

    sum_axis0 = np.sum(array_3x3, axis=0)
    sum_axis1 = np.sum(array_3x3, axis=1)
    sum_flattened = np.sum(array_3x3)

    calculations = {
        "mean": [mean_axis0.tolist(), mean_axis1.tolist(), mean_flattened.tolist()],
        "variance": [var_axis0.tolist(), var_axis1.tolist(), var_flattened.tolist()],
        "standard deviation": [
            std_axis0.tolist(),
            std_axis1.tolist(),
            std_flattened.tolist(),
        ],
        "max": [max_axis0.tolist(), max_axis1.tolist(), max_flattened.tolist()],
        "min": [min_axis0.tolist(), min_axis1.tolist(), min_flattened.tolist()],
        "sum": [sum_axis0.tolist(), sum_axis1.tolist(), sum_flattened.tolist()],
    }

    return calculations
