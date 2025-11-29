v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 9 + 7
v4 = 0
for v5 in range(v1):
    for v6 in range(v5 + 1, v1):
        v4 += v2[v5] * v2[v6]
        v4 %= v3
print(v4)
