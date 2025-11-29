v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = 0
v5 = 0
for v3 in range(0, v1):
    v4 += v2[v3]
    v5 += v2[v3] ** 2
v4 = v4 ** 2
v6 = (v4 - v5) / 2
print(int(v6 % 1000000007))
