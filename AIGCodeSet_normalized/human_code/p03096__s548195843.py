v1 = {i: 0 for v2 in range(1 << 18)}
v3 = 0
v4 = 1
for v5 in [0] * int(input()):
    v6 = int(input())
    v4 += v1[v6] * (v3 != v6)
    v1[v6] = v4
    v3 = v6
print(v4 % (10 ** 9 + 7))
