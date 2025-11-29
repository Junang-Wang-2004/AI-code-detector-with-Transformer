v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000
for v4 in range(len(v2) - 1):
    v5 = v3 // v2[v4]
    if v2[v4] < v2[v4 + 1]:
        v3 -= v5 * v2[v4]
        v3 += v2[v4 + 1] * v5
print(v3)
