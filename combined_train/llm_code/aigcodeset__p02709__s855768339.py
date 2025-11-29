import sys
sys.setrecursionlimit(2 ** 2000)
v1 = int(input())
v2 = list(map(int, input().split()))
v2 = [(i, v) for v3, v4 in enumerate(v2)]
v2.sort(key=lambda x: x[1], reverse=True)
v5 = [[-1] * (m + 1) for v6 in range(v1 + 1)]

def f1(a1, a2):
    if a1 == v1:
        return 0
    if v5[a1][a2] != -1:
        return v5[a1][a2]
    v1 = v1 - a1 + a2 - 1
    v2, v3 = v2[a1]
    if v2 >= a2:
        v5[a1 + 1][a2 + 1] = f1(a1 + 1, a2 + 1)
    if v2 <= v1:
        v5[a1 + 1][a2] = f1(a1 + 1, a2)
    return max(v5[a1 + 1][a2 + 1] + v3 * (v2 - a2), v5[a1 + 1][a2] + v3 * (v1 - v2))
print(f1(0, 0))
