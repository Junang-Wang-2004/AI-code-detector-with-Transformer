v1, v2 = map(int, input().split())
v3 = [i for v4 in range(v1 + 1)]
v5 = 0
v6 = 10 ** 9 + 7
for v4 in range(v2, v1 + 2):
    v7 = (v1 - v4 + 1) * v4 + 1
    v5 += v7
print(v5 % v6)
