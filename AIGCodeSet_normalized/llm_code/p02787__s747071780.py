from operator import itemgetter
v1, v2 = map(int, input().split())
v3 = []
v4 = 0
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v4 = max(v6, v4)
    v3.append([v6 / v7, v6, v7])
v3.sort(key=itemgetter(0), reverse=True)
v3.sort(key=itemgetter(1), reverse=True)
v8 = 0

def f1(a1, a2, a3):
    if a1 == 0:
        return 0
    for v1 in v3[a2:]:
        if a1 < v1[1]:
            continue
        else:
            v2 = a1 // v1[1]
            v3 = a1 - v2 * v1[1]
            return min(a3, v2 * v1[2] + f1(v3, a2 + 1, v1[2]))
    v4 = a3
    for v1 in v3[a2:]:
        v4 = min(v4, v1[2])
    return v4
v8 = f1(v1, 0, 10 ** 9)
print(v8)
