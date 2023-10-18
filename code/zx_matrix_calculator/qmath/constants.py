import numpy as np

Q_ZERO = np.array([[1, 0]], dtype=complex).T
Q_ONE = np.array([[0, 1]], dtype=complex).T

Q_PLUS = 1 / np.sqrt(2) * (Q_ZERO + Q_ONE)
Q_MINUS = 1 / np.sqrt(2) * (np.subtract(Q_ZERO, Q_ONE))
