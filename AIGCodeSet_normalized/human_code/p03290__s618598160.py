v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append([v5, v6])

def f1(a1, a2):
    if a2 < 0:
        return 10 ** 9
    v1 = min(a1 // (100 * (a2 + 1)), v3[a2][0])
    v2 = 100 * (a2 + 1) * v1
    if v1 == v3[a2][0]:
        v2 += v3[a2][1]
    if v2 < a1:
        v3 = v1 + f1(a1 - v2, a2 - 1)
    else:
        v3 = v1
    return min(v3, f1(a1, a2 - 1))
print(f1(v2, v1 - 1))
