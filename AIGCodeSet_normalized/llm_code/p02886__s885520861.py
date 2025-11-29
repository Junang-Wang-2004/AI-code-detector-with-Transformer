v1 = int(input())
v2 = list(map(int, input().split()))
sum = 0
for v3 in range(v1):
    for v4 in range(v3 + 1, v1):
        sum += v2[v3] * v2[v4]
print(sum)
