from typing import List, cast

import numpy as np

from qmath.tensor import tensor


def compose(*steps: List[np.ndarray]) -> np.ndarray:
    """
    Composes a list of matrices. Steps get combined using matrix multiplication. 
    Order: From Last Step to First Step.
    Elements in each step get combined using tensor product.
    """

    combination_result = 1

    for step in steps[::-1]:
        step_result = np.array([[1]], dtype=complex)
        for element in step:
            step_result = tensor(step_result, element)

        combination_result = np.dot(combination_result, step_result)

    return cast(np.ndarray, combination_result)
