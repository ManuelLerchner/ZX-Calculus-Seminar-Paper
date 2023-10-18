import numpy as np
from qmath.tensor import tensor_repeat, tensor
from zx_helper.compose import compose
from zx_helper.spider import spider
from qmath.constants import Q_MINUS, Q_ONE, Q_PLUS, Q_ZERO

np.set_printoptions(precision=3, suppress=True)

IDENTITY = spider(1, 1, "red")

CUP = spider(0, 2, "red")
CAP = spider(2, 0, "red")

R21 = spider(2, 1, "red")
G12 = spider(1, 2, "green")
G21 = spider(2, 1, "green")
R12 = spider(1, 2, "red")

CNOT_C0 = compose([IDENTITY, R12], [G21, IDENTITY])
CNOT_C1 = compose([IDENTITY, G12], [R21, IDENTITY])

ZERO = spider(0, 1, "red")
ONE = spider(0, 1, "red", np.pi)
PLUS = spider(0, 1, "green")
MINUS = spider(0, 1, "green", np.pi)


HADAMARD = compose([spider(1, 1, "green", np.pi / 2)],
                   [spider(1, 1, "red", np.pi / 2)],
                   [spider(1, 1, "green", np.pi / 2)])

SWAP = compose([CNOT_C0], [CNOT_C1], [CNOT_C0])

HOPF_RULE = compose([R21], [G12])
HOPF_RESULT = compose([spider(0, 1, "red")], [spider(1, 0, "green")])


print(CNOT_C0)


Z = spider(1, 1, "green", np.pi)
X = spider(1, 1, "red", np.pi)

print(compose([Z], [X]))
