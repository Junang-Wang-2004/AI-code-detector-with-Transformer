v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(len(v2)):
    v3 += v2[v4] * sum(v2[v4 + 1:])
print(v3)
