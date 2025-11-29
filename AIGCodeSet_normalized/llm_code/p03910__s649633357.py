v1 = int(input())
v2 = 0
for v3 in range(1, v1 + 1):
    v4 = v3 * (v3 - 1) // 2
    if v4 >= v1:
        v2 = v3 - 1
        break
v5 = [v3 for v3 in range(v2, 0, -1)]
v4 = v1 - v5[0]
print(v5[0])
for v3 in range(1, len(v5)):
    if v4 == 0:
        break
    v4 -= v5[v3]
    print(v5[v3])
