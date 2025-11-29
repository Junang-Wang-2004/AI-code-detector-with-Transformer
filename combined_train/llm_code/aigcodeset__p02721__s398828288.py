import sys
sys.setrecursionlimit(10 ** 6)
v1 = lambda x: int(x) - 1
v2 = lambda x: print(*x, sep='\n')

def f1():
    return int(sys.stdin.readline())

def f2():
    return map(int, sys.stdin.readline().split())

def f3():
    return list(map(int, sys.stdin.readline().split()))

def f4(a1):
    return [f3() for v1 in range(a1)]

def f5():
    return sys.stdin.readline()[:-1]

def f6():
    v1, v2, v3 = f2()
    v4 = f5()
    v5 = [0] * v1
    v6 = [0] * v1
    for v7, v8 in enumerate(v4):
        if v8 == 'o':
            if v7 - v3 - 1 >= 0:
                v5[v7] = v5[v7 - v3 - 1] + 1
            else:
                v5[v7] = 1
        else:
            v5[v7] = v5[v7 - 1]
    for v7 in range(v1 - 1, -1, -1):
        v8 = v4[v7]
        if v8 == 'o':
            if v7 + v3 + 1 < v1:
                v6[v7] = v6[v7 + v3 + 1] + 1
            else:
                v6[v7] = 1
        else:
            v6[v7] = v6[(v7 + 1) % v1]
    v9 = []
    if v6[1] < v2:
        v9.append(1)
    for v7 in range(1, v1 - 1):
        if v5[v7 - 1] + v6[v7 + 1] < v2:
            v9.append(v7 + 1)
    if v1 - 2 >= 0 and v5[v1 - 2] < v2:
        v9.append(v1)
    print(*v9, sep='\n')
f6()
