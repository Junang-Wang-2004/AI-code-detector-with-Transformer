v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [(x, i) for v4, v5 in enumerate(v2)]
v3.sort()
v6 = [[-1] * v1 for v7 in range(v1)]

def f1(a1, a2):
    if a2 < a1:
        return 0
    if v6[a1][a2] >= 0:
        return v6[a1][a2]
    v1 = a2 - a1
    v2, v3 = v3[v1]
    v4 = v2 * abs(a1 - v3)
    v5 = v2 * abs(a2 - v3)
    v6 = v6[a1][a2] = max(v4 + f1(a1 + 1, a2), v5 + f1(a1, a2 - 1))
    return v6
print(f1(0, v1 - 1))
