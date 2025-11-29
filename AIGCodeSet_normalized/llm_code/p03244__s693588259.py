v1 = int(input())
v2 = [int(x) for v3 in input().split()]
v4 = [0] * 10 ** 5
v5 = [0] * 10 ** 5
for v6 in range(v1):
    if v6 % 2:
        v4[v2[v6]] += 1
    else:
        v5[v2[v6]] += 1
v7 = v4.index(max(v4)) if max(v4) != 0 else 0
v8 = v5.index(max(v5)) if max(v5) != 0 else 0
v9 = sorted(v4, reverse=True)
v10 = sorted(v5, reverse=True)
v6 = 1
v11 = 0
if v7 == v8:
    v11 += min(v9[0], v10[0])
while v6 < len(v9) and v6 < len(v10) and (v9[v6] != 0 or v10[v6] != 0):
    if v9[v6] != 0:
        v11 += v9[v6]
    if v10[v6] != 0:
        v11 += v10[v6]
    v6 += 1
print(v11)
