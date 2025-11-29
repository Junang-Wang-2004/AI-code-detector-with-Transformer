v1 = int(input())
v2 = [True] * 100001
for v3 in range(2, 100001):
    if v2[v3]:
        for v4 in range(v3 * v3, 100001, v3):
            v2[v4] = False
v2[1], v2[2] = (False, True)
v5 = [0] * 100002
for v4 in range(1, 100001):
    if v2[v4] and v2[(v4 + 1) // 2]:
        v5[v4] = v5[v4 - 1] + 1
    else:
        v5[v4] = v5[v4 - 1]
for v4 in range(v1):
    v6, v7 = map(int, input().split())
    print(v5[v7] - v5[v6 - 1])
