from itertools import groupby
v1 = input()
v2 = [len(list(it)) for v3, v4 in groupby(v1)]
v5 = []
for v6, v7 in zip(v2[::2], v2[1::2]):
    v5.extend([0] * (v6 - 1) + [(v6 + 1) // 2 + v7 // 2] + [v6 // 2 + (v7 + 1) // 2] + [0] * (v7 - 1))
print(*v5)
