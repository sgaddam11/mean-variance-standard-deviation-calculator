import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    li_of_li = [list[i:i + 3] for i in range(0, len(list), 3)]
    arr = np.array(li_of_li)

    # mean
    axis1 = np.mean(arr, axis=0).tolist()
    axis2 = np.mean(arr, axis=1).tolist()
    flattened = np.mean(arr).tolist()
    # variance
    var_axis1 = np.var(arr, axis=0).tolist()
    var_axis2 = np.var(arr, axis=1).tolist()
    var_flat = np.var(arr).tolist()
    # str deviation
    std_axis1 = np.std(arr, axis=0).tolist()
    std_axis2 = np.std(arr, axis=1).tolist()
    std_flat = np.std(arr).tolist()
    # min and max
    min_axis1 = np.min(arr, axis=0).tolist()
    min_axis2 = np.min(arr, axis=1).tolist()
    min_flat = np.min(arr).tolist()
    max_axis1 = np.max(arr, axis=0).tolist()
    max_axis2 = np.max(arr, axis=1).tolist()
    max_flat = np.max(arr).tolist()
    # sum
    sum_axis1 = np.sum(arr, axis=0).tolist()
    sum_axis2 = np.sum(arr, axis=1).tolist()
    sum_flat = np.sum(arr).tolist()

    calculations = {
        'mean': [axis1, axis2, flattened],
        'variance': [var_axis1, var_axis2, var_flat],
        'standard deviation': [std_axis1, std_axis2, std_flat],
        'max': [max_axis1, max_axis2, max_flat],
        'min': [min_axis1, min_axis2, min_flat],
        'sum': [sum_axis1, sum_axis2, sum_flat]
    }

    return calculations