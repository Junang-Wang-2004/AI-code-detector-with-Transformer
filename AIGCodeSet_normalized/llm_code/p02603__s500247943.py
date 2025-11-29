v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000
v4 = 0
for v5 in range(v1 - 1):
    if v2[v5 + 1] > v2[v5]:
        v4 = v3 // v2[v5]
        v3 = v3 - v4 * v2[v5]
    else:
        v3 += v4 * v2[v5]
        v4 = 0
v3 += v4 * v2[v1 - 1]
print(v3)
