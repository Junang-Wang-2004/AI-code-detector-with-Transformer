v1, v2 = map(int, input().split())
v3 = v2 - v1
v4 = 0
for v5 in range(1, v3 + 1):
    v4 = v4 + v5
print(v4 - v2)
