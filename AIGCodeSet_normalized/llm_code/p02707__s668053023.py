import numpy as np
from numba import njit
v1 = int(input())
v2 = list(map(int, input().split()))

@njit
def f1(a1, a2):
    v1 = a1.count(a2)
    print(v1)
print(v1 - 1)
for v3 in range(1, v1):
    f1(v2, v3)
