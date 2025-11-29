v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2[v4], v3[v4] = (v5, v6)
v7 = 0
for v4 in range(v1 - 1, -1, -1):
    if (v2[v4] + v7) % v3[v4] == 0:
        v8 = 0
    else:
        v8 = v3[v4] - (v2[v4] + v7) % v3[v4]
    v7 += v8
print(v7)
