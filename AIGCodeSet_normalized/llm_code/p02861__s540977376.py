import itertools, math, statistics
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    v2.append(v4)
v5 = itertools.permutations(v2)
v6 = []
for v7 in list(v5):
    v8 = 0
    for v9 in range(v1 - 1):
        v10 = math.sqrt((v7[v9][0] - v7[v9 + 1][0]) ** 2 + (v7[v9][1] - v7[v9 + 1][1]) ** 2)
        v8 += v10
    v6.append(v8)
print(statistics.mean(v6))
