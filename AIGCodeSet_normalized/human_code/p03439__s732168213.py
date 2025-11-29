v1 = {'Male': 1, 'Female': 2, 'Vacant': 0}

def f1(a1, a2, a3, a4):
    if a3 != a4:
        return (a2 - a1 + 1) % 2 == 1
    else:
        return (a2 - a1 + 1) % 2 == 0

def f2(a1):
    print(a1 - 1)
    return v1[input()]

def f3():
    v1 = int(input())
    v2 = f2(1)
    if v2 == 0:
        return
    v3 = f2(v1)
    if v3 == 0:
        return
    v4, v5 = (1, v1)
    while v4 + 2 < v5:
        v6 = (v4 + v5) // 2
        v7 = f2(v6)
        if v7 == 0:
            return
        if f1(v4, v6, v2, v7):
            v3, v5 = (v7, v6)
        else:
            v2, v4 = (v7, v6)
    f2(v4 + 1)
f3()
