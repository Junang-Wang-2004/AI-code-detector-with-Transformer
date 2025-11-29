import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def f1():
    v1, v2 = map(int, input().split())
    v3, v4 = map(int, input().split())
    v5, v6 = map(int, input().split())
    if (v3 - v5) * (v4 - v6) > 0:
        print(0)
        return
    v7 = v1 * abs(v5 - v3)
    v8 = v2 * abs(v6 - v4)
    if v7 == v8:
        print('infinity')
        return
    v9 = v7 % (v8 + v7)
    v10 = v7 // (v8 + v7)
    if v9 == 0:
        v11 = 2 * v10
    else:
        v11 = 2 * v10 + 1
    print(v11)
f1()
