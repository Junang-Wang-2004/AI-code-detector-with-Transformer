v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 + 1)
v3[0] = 1000
for v4 in range(1, v1 + 1):
    for v5 in range(v4):
        v3[v4] = max(v3[v4], v3[v5] + (v2[v4 - 1] - v2[v5 - 1]) * (v3[v5] // v2[v5 - 1]))
print(v3[v1])
