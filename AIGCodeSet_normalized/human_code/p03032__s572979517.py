v1, v2 = map(int, input().split())
*v3, = map(int, input().split())

def f1(a1, a2):
    v1 = []
    v2 = 0
    for v3 in range(a1):
        v1.append(v3[v3])
        v2 += v3[v3]
    for v3 in range(v1 - 1, v1 - a2 - 1, -1):
        v1.append(v3[v3])
        v2 += v3[v3]
    v1.sort()
    for v3 in range(min(v2 - a1 - a2, a1 + a2)):
        if v1[v3] >= 0:
            break
        v2 -= v1[v3]
    return v2
v4 = 0
for v5 in range(v2 + 1):
    for v6 in range(min(v2 - v5 + 1, v1 - v5 + 1)):
        v4 = max(v4, f1(v5, v6))
print(v4)
