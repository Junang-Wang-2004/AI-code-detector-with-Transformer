from collections import Counter
v1, v2, v3 = map(int, input().split())
v4 = [tuple(map(int, input().split())) for v5 in range(v3)]
v6 = set(v4)
v7 = Counter()
v8 = Counter()
for v9, v10 in v4:
    v8[v9] += 1
    v7[v10] += 1
v11 = 0
for v9, v10 in v4:
    v11 = max(v11, v8[v9] + v7[v10] - 1)
v12 = v7.most_common()
v13 = v8.most_common()
v14 = v12[0][1]
v15 = v13[0][1]
for v16, v17 in v12:
    if v17 < v14:
        break
    for v18, v19 in v13:
        if v19 < v15:
            break
        if (v18, v16) in v6:
            continue
        v11 = max(v11, v19 + v17)
        break
print(v11)
