import math

def f1(a1, a2, a3, a4):
    return sum([max([0, math.ceil((h - a3 * a1) // (a2 - a3))]) for v1 in a4]) <= a1

def f2():
    v1, v2, v3 = list(map(int, input().split(' ')))
    v4 = [int(input()) for v5 in range(v1)]
    v6, v7 = (0, 10 ** 9)
    while v7 - v6 > 1:
        v8 = (v7 + v6) // 2
        if f1(v8, v2, v3, v4):
            v7 = v8
        else:
            v6 = v8
    print(v7)
if __name__ == '__main__':
    f2()
