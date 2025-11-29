v1, v2 = map(int, input().split())
v3 = [[0 for v4 in range(v2)] for v5 in range(100000)]
for v6 in range(v1):
    v7, v8, v2 = map(int, input().split())
    for v5 in range(v7 - 1, v8):
        v3[v5][v2 - 1] = 1
v9 = 0
for v4 in range(100000):
    if sum(v3[v4]) > v9:
        v9 = sum(v3[v4])
print(v9)
