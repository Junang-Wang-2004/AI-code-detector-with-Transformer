v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 + 1)
for v4, v5 in enumerate(v2):
    v3[v5] = v4
v6 = 0
v7 = 0
for v4 in range(1, v1 + 1):
    if v3[v4] >= v3[v4 - 1]:
        v7 += 1
    else:
        v6 = max(v6, v7)
        v7 = 1
v6 = max(v6, v7)
print(v1 - v6)
