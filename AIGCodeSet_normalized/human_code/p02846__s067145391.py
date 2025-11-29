def f1():
    import math
    v1, v2 = map(int, input().split())
    v3, v4 = map(int, input().split())
    v5, v6 = map(int, input().split())
    v7 = (v3 - v5) * v1
    v8 = (v4 - v6) * v2
    v9 = v7 + v8
    if v7 == -v8:
        print('infinity')
        return
    elif v7 * v8 > 0 or abs(v7) > abs(v8):
        print(0)
        return
    v7 = abs(v7)
    v9 = abs(v9)
    v10 = v7 // v9
    v11 = v7 % v9
    if v11 == 0:
        print(v10 * 2)
    else:
        print(v10 * 2 + 1)
if __name__ == '__main__':
    f1()
