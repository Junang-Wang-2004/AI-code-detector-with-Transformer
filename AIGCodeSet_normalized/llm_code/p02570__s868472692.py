v1 = int(input())
v2 = [int(i) for v3 in input().split(' ')]
v4 = 1000000007
sum = 0
for v3 in v2:
    sum += v3
for v5, v3 in enumerate(v2[:-1]):
    sum -= v2[v5]
    sum += v3 * sum
print(sum % v4)
