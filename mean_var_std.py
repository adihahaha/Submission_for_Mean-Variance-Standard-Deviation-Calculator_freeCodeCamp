import numpy as np


def calculate(arr):
    flat_arr = np.array(arr)

    if len(arr) != 9:
        raise ValueError("List must contain nine numbers.")
        return

    main_arr = flat_arr.reshape(3, 3)
    result = {}
    result['mean'] = list([
        list(main_arr.mean(axis=0)),
        list(main_arr.mean(axis=1)),
        flat_arr.mean()
    ])

    result['variance'] = list([
        list(np.var(main_arr, axis=0)),
        list(np.var(main_arr, axis=1)),
        np.var(flat_arr),
    ])

    result['standard deviation'] = list([
        list(np.std(main_arr, axis=0)),
        list(np.std(main_arr, axis=1)),
        np.std(flat_arr),
    ])

    result['max'] = list([
        list(main_arr.max(axis=0)),
        list(main_arr.max(axis=1)),
        flat_arr.max(),
    ])

    result['min'] = list([
        list(main_arr.min(axis=0)),
        list(main_arr.min(axis=1)),
        flat_arr.min(),
    ])

    result['sum'] = list([
        list(main_arr.sum(axis=0)),
        list(main_arr.sum(axis=1)),
        flat_arr.sum(),
    ])
    return result
