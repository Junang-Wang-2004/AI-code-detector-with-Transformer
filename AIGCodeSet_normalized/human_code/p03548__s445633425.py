def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = v1 // (v2 + v3)
    if v4 * (v2 + v3) + v3 <= v1:
        print(v4)
    else:
        print(v4 - 1)
f1()
