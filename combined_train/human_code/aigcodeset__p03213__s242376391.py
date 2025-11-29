"""
22:17:30

"""
from collections import defaultdict
v1 = int(input())

def f1(a1):
    if not isinstance(a1, int):
        raise TypeError('Input int')
    if a1 < 2:
        raise ValueError('N >= 2')
    v1 = []
    v2 = [i + 1 for v3 in range(1, a1)]
    while True:
        v4 = v2[0]
        if v4 >= int(a1 ** 0.5):
            return v1 + v2
        v1.append(v4)
        v2 = [d for v5 in v2 if v5 % v4 != 0]

def f2(a1):
    v1 = defaultdict(int)
    for v2 in range(1, a1 + 1):
        if v2 <= 3:
            v1[v2] += 1
            continue
        v3 = f1(int(v2 ** 0.5))
        for v4 in v3:
            while v2 % v4 == 0:
                v1[v4] += 1
                v2 //= v4
        if v2 != 1:
            v1[v2] += 1
    return v1
v2 = f2(v1)
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
for v8 in v2.keys():
    v9 = v2[v8]
    if v9 >= 2:
        v7 += 1
    if v9 >= 4:
        v6 += 1
    if v9 >= 14:
        v5 += 1
    if v9 >= 24:
        v4 += 1
    if v9 >= 74:
        v3 += 1
v10 = 0
v10 += v3
v10 += (v7 - 1) * v4
v10 += (v6 - 1) * v5
v10 += (v7 - 2) * v6 * (v6 - 1) // 2
print(v10)
