def f1():
    v1, v2, v3 = map(int, input().split())
    return (v1, v2, v3)

def f2(a1, a2, a3):
    v1 = (a1 - a3) // (a2 + a3)
    print(v1)

def f3():
    v1, v2, v3 = f1()
    f2(v1, v2, v3)
f3()
