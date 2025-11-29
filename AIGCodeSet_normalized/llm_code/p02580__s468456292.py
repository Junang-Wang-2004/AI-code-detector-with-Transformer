from collections import Counter
v1, v2, v3 = map(int, input().split())
v4, v5 = ({}, {})
v6, v7 = (Counter(), Counter())
for v8 in range(v3):
    v9, v10 = map(int, input().split())
    v6[v9] += 1
    v7[v10] += 1
    if v9 in v4:
        v4[v9].add(v10)
    else:
        v4[v9] = {v10}
    if v10 in v5:
        v5[v10].add(v9)
    else:
        v5[v10] = {v9}
v11 = 0
for v12 in v4.keys():
    v13 = v4[v12]
    v14 = len(v13)
    for v15 in v13:
        v16 = v14 + v7[v15] - 1
        v11 = max(v16, v11)
v6 = [(k, v15) for v17, v15 in v6.items()]
v7 = [(v17, v15) for v17, v15 in v7.items()]
v6.sort(key=lambda x: x[1], reverse=True)
v7.sort(key=lambda x: x[1], reverse=True)
v6 = v6[:30]
v7 = v7[:30]
for v18 in v6:
    for v19 in v7:
        v20, v21 = (v18[0], v19[0])
        if v20 in v4 and v21 in v5 and (v21 not in v4[v20]):
            v16 = len(v4[v20]) + v7[v21]
            v11 = max(v16, v11)
print(v11)
