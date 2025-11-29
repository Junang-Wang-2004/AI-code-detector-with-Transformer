v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v2, v1 + 2):
    v3 += (v1 + v1 - v4 + 1) * v4 // 2 - (v4 - 1) * (v4 // 2) + 1
print(v3 % (10 ** 9 + 7))
