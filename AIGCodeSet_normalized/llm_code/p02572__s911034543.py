v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(0, v1 - 1):
    for v5 in range(v4 + 1, v1):
        v3 += v2[v4] * v2[v5]
print(v3 % (10 ** 9 + 7))
