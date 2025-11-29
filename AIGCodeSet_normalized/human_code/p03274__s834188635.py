v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
for v5 in range(v1 - v2 + 1):
    v6 = v3[v5]
    v7 = v3[v5 + v2 - 1]
    v8 = v7 - v6
    v9, v10 = (abs(v6), abs(v7))
    if v9 > v10:
        v8 += v10
    else:
        v8 += v9
    v4.append(v8)
print(min(v4))
