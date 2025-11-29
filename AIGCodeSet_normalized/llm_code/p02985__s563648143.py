import sys
sys.setrecursionlimit(1000000)

def f1(a1, a2):
    v1 = [[] for v2 in range(a1)]
    for v3, v4 in a2:
        v1[v3 - 1] += [v4 - 1]
        v1[v4 - 1] += [v3 - 1]
    return v1

def f2(a1, a2, a3, a4, a5):
    v1 = 1000000007
    if a4 == -1:
        v2 = a1 - 1
    else:
        v2 = a1 - 2
    if len(a2[a3]) > v2:
        return 0
    for v3 in a2[a3]:
        if v3 == a4:
            continue
        else:
            a5 *= v2
            v2 -= 1
            a5 %= v1
    for v3 in a2[a3]:
        if v3 == a4:
            continue
        else:
            a5 = f2(a1, a2, v3, a3, a5)
    return a5 % v1
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    v3 = [None] * (v1 - 1)
    for v4 in range(v1 - 1):
        v3[v4] = list(map(int, input().split()))
    v5 = f1(v1, v3)
    print(f2(v2, v5, 0, -1, v2))
