import sys
from collections import Counter
from functools import reduce

def f1():
    return input()
v1 = f1()
v2 = len(v1)
v3 = [set() for v4 in range(v2)]
for v5 in range(v2):
    v3[v5].add(v1[v5])
for v5 in range(v2 - 1, 0, -1):
    for v6 in range(v5):
        v3[v6] |= v3[v6 + 1]
    v7 = v3[0]
    if len(v7) == 1:
        print(v2 - v5)
        break
