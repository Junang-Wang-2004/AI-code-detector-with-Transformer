v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in range(v1):
    v3 += v2[v5]
    v4 += v2[v5] * v2[v5]
v3 = v3 * v3 - v4
v3 = v3 // 2
v3 = v3 % (10 ** 9 + 7)
print(v3)
