import sys
import itertools
import numpy as np
from collections import defaultdict
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
v4 = int(v2())
v5 = list(map(lambda x: x.split(), v1().decode().split('\n')))
v6 = defaultdict(list)
v7 = {}
v8 = {}
for v9 in range(v4):
    v10 = None
    for v11 in range(v4 - 1):
        if v9 + 1 < int(v5[v9][v11]):
            v12 = '{}-{}'.format(v9 + 1, v5[v9][v11])
        else:
            v12 = '{}-{}'.format(v5[v9][v11], v9 + 1)
        if v10:
            v6[v10].append(v12)
        v10 = v12
        v7[v12] = False
        v8[v12] = 0

def f1(a1):
    if v7[a1]:
        return v8[a1]
    v7[a1] = True
    v8[a1] = 0
    for v1 in v6[a1]:
        v8[a1] = max(v8[a1], f1(v1) + 1)
    return v8[a1]
v13 = 0
for v12 in list(v6):
    v13 = max(f1(v12), v13)
print(v13 + 1)
