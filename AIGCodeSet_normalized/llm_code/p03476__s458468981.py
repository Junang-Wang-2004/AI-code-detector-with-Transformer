def f1(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = False
    v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if not v1[v2]:
            continue
        for v3 in range(v2 * 2, a1 + 1, v2):
            v1[v3] = False
    return ([v2 for v2 in range(a1 + 1) if v1[v2]], v1)
v1, v2 = f1(10 ** 5 + 1)
for v3 in v1:
    if v2[(v3 + 1) // 2]:
        v2[v3] = False
v4 = [0] * (10 ** 5 + 1)
for v3 in range(10 ** 5 + 1):
    if v3 == 0:
        continue
    if v2[v3]:
        v4[v3] = v4[v3 - 1] + 1
    else:
        v4[v3] = v4[v3 - 1]
v5 = int(input())
for v6 in range(v5):
    v7, v8 = map(int, input().split())
    if v7 > 0:
        print(v4[v8] - v4[v7 - 1])
    else:
        print(v4[v8])
