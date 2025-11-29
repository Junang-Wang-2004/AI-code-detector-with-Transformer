v1 = int(input())
v2 = list(map(int, input().split()))
v3 = False
v4 = []
for v5 in range(v1 - 1):
    if v2[v5] > v2[v5 + 1]:
        if v3:
            v4.append(v2[v5])
        v3 = False
    elif v2[v5] < v2[v5 + 1]:
        if not v3:
            v4.append(v2[v5])
        v3 = True
    else:
        pass
else:
    if v3:
        v4.append(v2[-1])
v6 = len(v4)
v7 = 1000
v8 = 0
for v5 in range(v6):
    if v5 % 2 == 0:
        v8 = v7 // v4[v5]
        v7 = v7 - v8 * v4[v5]
    else:
        v7 += v8 * v4[v5]
print(v7)
