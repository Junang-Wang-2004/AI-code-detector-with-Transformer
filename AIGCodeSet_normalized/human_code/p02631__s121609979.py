v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    v3 ^= v4
v5 = []
for v4 in v2:
    v5.append(v3 ^ v4)
print(*v5)
