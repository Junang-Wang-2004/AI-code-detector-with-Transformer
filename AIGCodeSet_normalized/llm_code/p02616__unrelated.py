import sys
v1 = 10 ** 9 + 7
v2, v3 = map(int, sys.stdin.readline().split())
v4 = list(map(int, sys.stdin.readline().split()))
v4.sort()
v5 = 0
for v6 in range(v2):
    if v4[v6] < 0:
        v5 += 1
if v3 == v2:
    v7 = 1
    for v6 in range(v2):
        v7 = v7 * v4[v6] % v1
    print(v7)
elif v5 % 2 == 0 or v5 == 0:
    v7 = 1
    for v6 in range(v2 - v3, v2):
        v7 = v7 * v4[v6] % v1
    print(v7)
else:
    v7 = 1
    for v6 in range(v2 - v3 + 1, v2):
        v7 = v7 * v4[v6] % v1
    print(v7)
