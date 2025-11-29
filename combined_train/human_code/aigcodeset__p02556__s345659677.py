v1 = int(input())
v2 = [] * v1
v3 = [] * v1
for v4 in range(v1):
    v5, v6 = list(map(int, input().split()))
    v2.append(v5)
    v3.append(v6)
v7 = v2[0] + v3[0]
v8 = v2[0] + v3[0]
for v4 in range(v1):
    if v2[v4] + v3[v4] > v8:
        v8 = v2[v4] + v3[v4]
    if v2[v4] + v3[v4] < v7:
        v7 = v2[v4] + v3[v4]
v9 = v8 - v7
v10 = 10 ** 9 - v2[v4] + v3[v4]
v11 = 10 ** 9 - v2[v4] + v3[v4]
for v4 in range(v1):
    if 10 ** 9 - v2[v4] + v3[v4] > v11:
        v11 = 10 ** 9 - v2[v4] + v3[v4]
    if 10 ** 9 - v2[v4] + v3[v4] < v10:
        v10 = 10 ** 9 - v2[v4] + v3[v4]
if v11 - v10 > v9:
    v9 = v11 - v10
print(v9)
