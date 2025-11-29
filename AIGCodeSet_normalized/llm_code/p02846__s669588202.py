import math

def f1():
    v1, v2 = map(int, input().split())
    v3, v4 = map(int, input().split())
    v5, v6 = map(int, input().split())
    v7 = v1 * v3 + v2 * v4
    v8 = v1 * v5 + v2 * v6
    if v7 == v8:
        return 'infinity'
    if v7 < v8:
        v7, v8 = (v8, v7)
        v3, v5 = (v5, v3)
        v4, v6 = (v6, v4)
    v9 = v1 * v3
    v10 = v1 * v5
    if v9 > v10:
        return 0
    v11, v12 = divmod((v10 - v9) // (v7 - v8))
    if v12 == 0:
        return v11 * 2
    return v11 * 2 + 1
print(f1())
