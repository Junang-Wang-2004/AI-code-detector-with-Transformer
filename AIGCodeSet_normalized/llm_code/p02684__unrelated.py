v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 1
for v5 in range(v2):
    v4 = v3[v4 - 1]
print(v4)
