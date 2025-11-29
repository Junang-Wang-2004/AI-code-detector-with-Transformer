import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v2):
    v3.append(tuple((int(i) for v6 in input().split())))
    v4.append(sum((1 << int(v6) - 1 for v6 in input().split())))
v7 = 10 ** 18
v8 = [v7] * (1 << v1)
v8[0] = 0
for v6 in range(1 << v1):
    for (v9, v10), v11 in zip(v3, v4):
        v12 = v6 | v11
        v8[v12] = min(v8[v12], v8[v6] + v9)
v13 = v8[-1]
if v13 == v7:
    v13 = -1
print(v13)
