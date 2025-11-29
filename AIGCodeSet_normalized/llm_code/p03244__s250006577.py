from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[::2]
v4 = v2[1::2]
v5 = sorted(Counter(v3).items(), key=lambda x: x[1], reverse=True)
v6 = sorted(Counter(v4).items(), key=lambda x: x[1], reverse=True)
v7 = max(v5, key=lambda x: x[1])[0]
v8 = max(v6, key=lambda x: x[1])[0]
v9 = 0
if v7 != v8:
    for v10 in range(v1 // 2):
        if v3[v10] != v7:
            v9 += 1
        if v4[v10] != v8:
            v9 += 1
elif v7 == v8 and len(v5) == 1 and (len(v6) == 1):
    v9 = v1 // 2
else:
    v11 = 0
    v12 = 0
    if len(v5) > 1:
        v7 = v5[1][0]
    for v10 in range(v1 // 2):
        if v3[v10] != v7:
            v11 += 1
        if v4[v10] != v8:
            v11 += 1
    if len(v6) > 1:
        v8 = v6[1][0]
    for v10 in range(v1 // 2):
        if v3[v10] != v7:
            v12 += 1
        if v4[v10] != v8:
            v12 += 1
    v9 = min(v11, v12)
print(v9)
