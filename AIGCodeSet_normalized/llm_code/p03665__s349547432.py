v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = [v4 % 2 for v4 in v3]
v6 = v5.count(1)
if v2 == 0:
    v7 = 2 ** (v1 - v6)
elif v6 == 0:
    v7 = 0
else:
    v7 = 2 ** (v1 - 1) - 2 ** (v1 - v6)
print(v7)
