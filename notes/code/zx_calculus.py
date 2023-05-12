import numpy as np
from zx_helper.compose import compose
from zx_helper.spider import spider
from constants import Q_MINUS, Q_ONE, Q_PLUS, Q_ZERO

np.set_printoptions(precision=3, suppress=True)


IDENTITY = spider(1, 1, "red")

CUP = spider(0, 2, "red")
CAP = spider(2, 0, "red")

R21 = spider(2, 1, "red")
G12 = spider(1, 2, "green")
G21 = spider(2, 1, "green")
R12 = spider(1, 2, "red")

CNOT_C0 = compose([IDENTITY, R21], [G12, IDENTITY])
CNOT_C1 = compose([IDENTITY, G21], [R12, IDENTITY])

ZERO = spider(0, 1, "red")
ONE = spider(0, 1, "red", np.pi)
PLUS = spider(0, 1, "green")
MINUS = spider(0, 1, "green", np.pi)


HADAMARD = compose([spider(1, 1, "green", np.pi / 2)],
                   [spider(1, 1, "red", np.pi / 2)],
                   [spider(1, 1, "green", np.pi / 2)])


SWAP = compose([CNOT_C0], [CNOT_C1], [CNOT_C0])

# apply Cnot to |10> ----> |11>
# print(compose([CNOT_C0], [ONE, ZERO]))

# print(Q_PLUS.T @ Q_PLUS)

print(CNOT_C0)
