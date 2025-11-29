import sys
sys.setrecursionlimit(10 ** 6)

def f1(a1, a2):
    if a2[a1] == a1:
        return a1
    a2[a1] = f1(a2[a1], a2)
    return a2[a1]

def f2(a1, a2, a3, a4):
    v1 = f1(a1, a3)
    v2 = f1(a2, a3)
    if v1 == v2:
        return
    if a4[v1] < a4[v2]:
        a3[v1] = v2
    elif a4[v1] > a4[v2]:
        a3[v2] = v1
    else:
        a3[v2] = v1
        a4[v1] += 1

def f3():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = [i for v5 in range(v1 + 1)]
    v6 = [0] * (v1 + 1)
    for v7 in range(v2):
        v8, v9 = map(int, input().split())
        f2(v8, v9, v4, v6)
    v10 = [0] * (v1 + 1)
    for v5 in range(1, v1 + 1):
        v11 = f1(v5, v4)
        v10[v11] += 1
    v12 = 0
    for v5 in range(1, v1 + 1):
        if v3[v5 - 1] == v5 or v10[f1(v5, v4)] % 2 == 0:
            v12 += 1
    print(v12)
f3()
