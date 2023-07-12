import numpy as np


def tensor(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Computes the tensor product of two matrices.
    """

    # Compute the tensor product of the two matrices

    return np.kron(A, B)


def tensor_repeat(A: np.ndarray, n: int) -> np.ndarray:
    """
    Computes the tensor product of a matrix with itself n times.
    """

    result = np.array([[1]], dtype=complex)
    for _ in range(n):
        result = tensor(result, A)

    return result
