v1 = int(input())
v2 = []
v3 = []
v4 = 0
for v5 in range(v1):
    v6 = list(map(int, input().split()))
    v2.append(v6[0])
    v3.append(v6[1])
for v7 in range(v1 - 1, -1, -1):
    if (v2[v7] + v4) % v3[v7] != 0:
        v4 += v3[v7] - (v2[v7] + v4) % v3[v7]
print(v4)
