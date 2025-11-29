import numpy as np
from copy import copy
v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1, a2):
    v1 = 0
    while a1 % a2 == 0:
        a1 = a1 / a2
        v1 += 1
    return v1
v3 = []
for v4 in v2:
    v5 = f1(v4, 2)
    v3.append(v5)
print(sum(v3))
