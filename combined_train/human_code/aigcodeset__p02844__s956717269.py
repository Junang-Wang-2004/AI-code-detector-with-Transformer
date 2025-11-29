from bisect import bisect_left
v1 = int(input())
v2 = input()
v3 = [[] for v4 in range(10)]
for v4 in range(v1):
    v5 = int(v2[v4])
    v3[v5].append(v4)
v6 = 0
for v4 in range(10 ** 3):
    v7 = v4 // 100
    v8 = (v4 - 100 * v7) // 10
    v9 = v4 - 100 * v7 - 10 * v8
    v10 = [0 for v4 in range(10)]
    if not v3[v7]:
        continue
    v11 = v3[v7][0]
    v10[v7] += 1
    if v10[v8] > len(v3[v8]) - 1:
        continue
    v12 = bisect_left(v3[v8], v11, v10[v8], len(v3[v8]))
    if v12 == len(v3[v8]):
        continue
    v11 = v3[v8][v12]
    v10[v8] = v12 + 1
    if v10[v9] > len(v3[v9]) - 1:
        continue
    v12 = bisect_left(v3[v9], v11, v10[v9], len(v3[v9]))
    if v12 != len(v3[v9]):
        v6 += 1
print(v6)
