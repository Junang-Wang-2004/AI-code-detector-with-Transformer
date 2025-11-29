import sys
sys.setrecursionlimit(10000)
v1 = int(input())
*v2, = map(int, input().split())
v2 = [(a, i) for v3, v4 in enumerate(v2)]
v2.sort(reverse=True)
v5 = [[None for v6 in range(v1 + 1)] for v7 in range(v1 + 1)]

def f1(a1, a2):
    if a1 == a2:
        v5[a1][a2] = 0
    if v5[a1][a2] != None:
        return v5[a1][a2]
    v1, v2 = v2[v1 - (a2 - a1)]
    v3 = f1(a1 + 1, a2) + v1 * abs(v2 - a1)
    v4 = f1(a1, a2 - 1) + v1 * abs(v2 - (a2 - 1))
    v5[a1][a2] = max(v3, v4)
    return v5[a1][a2]
print(f1(0, v1))
