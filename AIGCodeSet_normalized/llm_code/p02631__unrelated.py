v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    v3 ^= v4
v5 = 0
for v4 in v2[:v1 // 2]:
    v5 ^= v4
v6 = [v3 ^ v5]
for v4 in v2[1:]:
    v6.append(v6[-1] ^ v4)
print(*v6)
