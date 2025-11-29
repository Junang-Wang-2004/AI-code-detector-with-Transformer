v1 = int(input())
v2 = list(map(int, input().split()))
v3 = {}
v4 = {}
for v5, v6 in enumerate(v2):
    if v5 % 2 == 0:
        if v6 not in v3:
            v3[v6] = 1
        else:
            v3[v6] += 1
    elif v6 not in v4:
        v4[v6] = 1
    else:
        v4[v6] += 1
v7 = list(v3.values())
v7.sort(reverse=True)
v8 = list(v4.values())
v8.sort(reverse=True)
v9 = v7[0]
if len(v7) == 1:
    v10 = 0
else:
    v10 = v7[1]
v11 = v8[0]
if len(v8) == 1:
    v12 = 0
else:
    v12 = v8[1]
v13 = min(len(v2) - v9 - v12, len(v2) - v10 - v11)
print(v13)
