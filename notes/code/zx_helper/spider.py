from typing import Literal
import numpy as np
from constants import Q_MINUS, Q_ONE, Q_PLUS, Q_ZERO
from qmath.tensor import tensor_repeat


# color either "red" or "green"
def spider(m: int, n: int, color: Literal["red", "green"],
           phase: float = 0) -> np.ndarray:
    """
    Converts a spider with m inputs and n outputs to a matrix.
    """

    if color == "red":
        Basis = [Q_PLUS, Q_MINUS]
    elif color == "green":
        Basis = [Q_ZERO, Q_ONE]
    else:
        raise ValueError("Invalid color.")

    vec1_m = tensor_repeat(Basis[0], m)
    vec1_n = tensor_repeat(Basis[0], n)

    M = np.dot(vec1_m, vec1_n.T)

    vec2_m = tensor_repeat(Basis[1], m)
    vec2_n = tensor_repeat(Basis[1], n)

    M += np.exp(1j * phase) * np.dot(vec2_m, vec2_n.T)

    return M
