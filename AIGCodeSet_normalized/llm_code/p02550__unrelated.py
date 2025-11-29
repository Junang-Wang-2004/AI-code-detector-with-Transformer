v1, v2, v3 = map(int, input().split())
sum = 0
v4 = v2
for v5 in range(v1):
    sum += v4
    v4 = v4 ** 2 % v3
print(sum)
