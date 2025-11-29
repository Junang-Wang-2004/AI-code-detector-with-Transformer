v1 = int(input())
v2 = []
v3 = []
v4 = 0
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v2.append(v6)
    v3.append(v7)
v8 = 0
v9 = 0
for v10 in range(v1):
    v6 = v2[v10]
    v7 = v3[v10]
    v6 += v9
    if v6 % v7 != 0:
        v9 += v7 - v6 % v7
    v8 += v9
print(v8)
