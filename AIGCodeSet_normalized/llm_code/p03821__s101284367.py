v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append(v5)
    v3.append(v6)
v7 = 0
for v4 in range(v1 - 1, -1, -1):
    v5 = v2[v4]
    v6 = v3[v4]
    if v6 == 1:
        continue
    if v6 % v5 == 0:
        continue
    if v7 > 0:
        v5 += v7
    v8 = v6 - v5 % v6
    v7 += v8
print(v7)
