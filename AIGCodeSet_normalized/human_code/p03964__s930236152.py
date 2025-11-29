v1 = int(input())
v2 = 1
v3 = 1
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v7 = max((v2 + v5 - 1) // v5, (v3 + v6 - 1) // v6)
    v2 = v5 * v7
    v3 = v6 * v7
print(v2 + v3)
