v1 = int(input())
v2 = {}
v3 = {}
v4 = 0
v5 = 0
while v4 < v1:
    v6 = list(map(int, input().split()))
    v7 = v6[0]
    v8 = v6[1]
    v2[str(v4)] = v7
    v3[str(v4)] = v8
    if v5 == 0 and v7 != v8:
        v5 = 1
    v4 += 1
v9 = 0
v10 = 0
for v4 in range(v1):
    if v5 == 0:
        v11 = max(v2, key=v2.get)
        v9 += v2[str(v11)]
        if len(v2) != 0:
            v2.pop(v11)
        if len(v3) != 0:
            v3.pop(v11)
        if len(v3) == 0:
            break
        v12 = max(v3, key=v3.get)
        v10 += max(v3.values())
        if len(v2) != 0:
            v2.pop(v12)
        if len(v3) != 0:
            v3.pop(v12)
        if len(v2) == 0:
            break
    else:
        v12 = max(v3, key=v3.get)
        v9 += v2[v12]
        if len(v2) != 0:
            v2.pop(v12)
        if len(v3) != 0:
            v3.pop(v12)
        if len(v3) == 0:
            break
        v12 = max(v3, key=v3.get)
        v10 += max(v3.values())
        if len(v2) != 0:
            v2.pop(v12)
        if len(v3) != 0:
            v3.pop(v12)
        if len(v3) == 0:
            break
print(v9, v10)
