def f1(a1):
    v1 = 0
    if len(a1) == 1:
        return a1
    for v2 in range(len(a1) - 1):
        if a1[v2] + 1 != a1[v2 + 1]:
            del a1[v2 + 1]
            v1 = 1
            break
    if v1 == 1:
        v3 = a1[v2:]
    else:
        v3 = a1[-1]
    return v3

def f2(a1, a2, a3=None):
    if a2 in a1:
        return a1.index(a2)
    else:
        return a3

def f3(a1):
    v1 = f2(a1, 1)
    if v1 is not None:
        return a1[v1:]
    else:
        return None

def f4():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = f3(v2)
    if v3 is not None:
        v4 = []
        while len(v4) != 1:
            v4 = f1(v3)
        print(len(v2) - len(v4))
    else:
        print(-1)
f4()
