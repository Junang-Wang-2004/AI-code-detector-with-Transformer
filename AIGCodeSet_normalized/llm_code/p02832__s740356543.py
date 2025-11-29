import math

def f1():
    return [int(s) for v1 in input().split()]

def f2():
    return int(input())

def f3():
    v1 = f2()
    v2 = f1()
    if len(v2) == 1:
        return 0
    v3 = 0
    v4 = 0
    v5 = 0
    while v5 < len(v2):
        if v4 >= v1:
            return v3
        if v4 + 1 == v2[v5]:
            v4 += 1
            v5 += 1
        else:
            v3 += 1
            v5 += 1
    if v4 < v1:
        return -1
    return v3
if __name__ == '__main__':
    print(f3())
