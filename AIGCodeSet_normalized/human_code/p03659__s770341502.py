v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = sum(v2)
v5 = 9999999999999999
for v6 in range(v1 - 1):
    v3 += v2[v6]
    v4 -= v2[v6]
    v5 = min(v5, abs(v3 - v4))
print(v5)
