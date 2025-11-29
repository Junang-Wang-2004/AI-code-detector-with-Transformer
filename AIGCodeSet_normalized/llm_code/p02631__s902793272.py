v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    v3 ^= v4
for v5 in range(v1):
    print(v3 ^ v2[v5], end=' ')
