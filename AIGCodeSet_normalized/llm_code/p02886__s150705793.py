v1 = int(input())
v2 = map(int, input().split())
v2 = list(v2)
v3 = 0
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        v3 = v3 + v2[v4] * v2[v5]
print(v3)
