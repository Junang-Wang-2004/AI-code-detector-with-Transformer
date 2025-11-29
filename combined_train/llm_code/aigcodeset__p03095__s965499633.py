import bisect
import itertools
v1 = int(input())
v2 = input()
v3 = {}
for v4 in range(v1):
    if v2[v4] in v3:
        v3[v2[v4]].append(v4)
    else:
        v3[v2[v4]] = [v4]
v5 = 0
v6 = 10 ** 9 + 7
v7 = []
for v8, v9 in v3.items():
    v7.append(len(v9) - bisect.bisect_left(v9, 0))
for v4 in range(1, 27):
    v10 = v5
    for v11 in itertools.combinations(v7, v4):
        v12 = 1
        for v13 in v11:
            v12 = v12 * v13 % v6
        v5 = (v5 + v12) % v6
    if v10 == v5:
        break
print(v5)
