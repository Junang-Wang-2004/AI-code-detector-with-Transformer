v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 10 ** 9 + 7
v5 = sum(v2)
v6 = 0
for v7 in range(v1):
    v6 += v2[v7]
    v3 += (v5 - v6) * v2[v7] % v4
print(v3 % v4)
