import numpy as np
from zx_helper.compose import compose
from zx_helper.spider import spider

np.set_printoptions(precision=3, suppress=True)


IDENTITY = spider(1, 1, "red")

CUP = spider(2, 0, "red")
CAP = spider(0, 2, "red")

R12 = spider(1, 2, "red")
G21 = spider(2, 1, "green")
G12 = spider(1, 2, "green")
R21 = spider(2, 1, "red")

CNOT_C0 = compose([IDENTITY, R12], [G21, IDENTITY])
CNOT_C1 = compose([IDENTITY, G12], [R21, IDENTITY])

ZERO = spider(1, 0, "red")
ONE = spider(1, 0, "red", np.pi)
PLUS = spider(1, 0, "green")
MINUS = spider(1, 0, "green", np.pi)


HADAMARD = compose([spider(1, 1, "green", np.pi / 2)],
                   [spider(1, 1, "red", np.pi / 2)],
                   [spider(1, 1, "green", np.pi / 2)])

#apply Cnot to |10> ----> |11>
print(compose([CNOT_C0], [ONE, ZERO]))
