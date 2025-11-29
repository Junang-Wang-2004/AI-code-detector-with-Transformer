v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000
v4 = 0
for v5 in range(v1):
    if v5 == v1 - 1:
        v3 += v4 * v2[v5]
        break
    if v2[v5] < v2[v5 + 1]:
        v6 = v3 // v2[v5]
        v3 -= v2[v5] * v6
        v4 += v6
    elif v2[v5] > v2[v5 + 1]:
        v3 += v2[v5] * v4
        v4 = 0
print(v3)
