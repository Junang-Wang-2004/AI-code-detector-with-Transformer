import sys
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000
v4 = 0
for v5 in range(v1 - 1):
    if v2[v5] < v2[v5 + 1]:
        v4 += v3 // v2[v5]
        v3 %= v2[v5]
    elif v2[v5] > v2[v5 + 1]:
        v3 += v4 * v2[v5]
        v4 = 0
v3 += v4 * v2[-1]
print(v3)
