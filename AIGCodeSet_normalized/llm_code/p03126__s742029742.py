v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = [0] * v2
for v4 in v3:
    v6 = list(map(int, v4.split()))
    for v7 in range(1, v6[0] + 1):
        v5[v6[v7] - 1] += 1
print(v5.count(v1))
