v1, v2 = map(int, input().split())
v3 = [False] * v1
for v4 in range(v2):
    v5 = input()
    v6 = [int(c) for v7 in input().split()]
    for v7 in v6:
        v3[v7 - 1] = True
print(v1 - sum((v7 for v7 in v3)))
