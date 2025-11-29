from itertools import combinations_with_replacement as comp_rplc
v1, v2, v3 = list(map(int, input().split()))
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v6 = 0
for v7 in comp_rplc(range(1, v2 + 1), v1):
    v8 = 0
    for v9, v10, v11, v12 in v4:
        if v7[v10 - 1] - v7[v9 - 1] == v11:
            v8 += v12
    v6 = max(v6, v8)
print(v6)
