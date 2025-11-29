v1 = int(input())
v2 = {}
for v3 in range(v1):
    v4 = int(input())
    if v4 in v2:
        v2[v4] += 1
    else:
        v2[v4] = 0
v5 = 0
for v6 in v2.values():
    if v6 % 2 != 1:
        v5 += 1
print(v5)
