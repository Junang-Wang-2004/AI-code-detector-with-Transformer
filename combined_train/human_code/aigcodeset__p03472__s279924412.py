v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = max(v3)
v4.sort(reverse=True)
v9 = False
v10 = 0
v11 = 0
for v12 in v4:
    if v8 < v12:
        v10 += v12
        v11 += 1
        if v10 >= v2:
            v9 = True
            break
if v9:
    print(v11)
else:
    v13 = -((v10 - v2) // v8) + v11
    print(v13)
