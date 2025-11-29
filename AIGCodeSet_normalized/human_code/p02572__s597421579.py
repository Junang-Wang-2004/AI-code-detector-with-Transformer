v1 = input()
v2 = list(map(int, input().split()))
v3 = sum(v2)
v4 = 0
for v5 in range(0, len(v2) - 1):
    v3 -= v2[v5]
    v4 += v2[v5] * v3
print(v4 % (10 ** 9 + 7))
