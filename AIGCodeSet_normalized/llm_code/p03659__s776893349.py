v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = sum(v2)
v5 = 10 ** 10
for v6 in range(1, v1):
    v3 += v2[v6 - 1]
    v4 -= v2[v6 - 1]
    v5 = min(v5, abs(v3 - v4))
print(v5)
