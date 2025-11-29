from itertools import combinations, permutations
v1 = int(input())
v2 = []
v3 = v1
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append((v5, v6))
for v7, v8 in combinations(v2, 2):
    v9, v10 = (v7[0] - v8[0], v7[1] - v8[1])
    if v9 != 0 or v10 != 0:
        v11 = 0
        for v12, v13 in permutations(v2, 2):
            v14, v15 = (v12[0] - v13[0], v12[1] - v13[1])
            if v14 == v9 and v15 == v10:
                v11 += 1
        v3 = min(v3, v1 - v11)
print(max(v3, 1))
