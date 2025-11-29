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
    v4 = [f3() for v5 in range(v1)]
    v6 = 10 ** 9
    v7 = [(0, 0, 0)]
    for v8, v9, v10 in v4[:v1 // 2]:
        v11 = len(v7)
        for v12 in range(v11):
            v13, v14, v15 = v7[v12]
            v7.append((v8 + v13, v9 + v14, v10 + v15))
    v7 = [(v8 * v3 - v9 * v2, v10) for v8, v9, v10 in v7]
    v16 = [(0, 0, 0)]
    for v8, v9, v10 in v4[v1 // 2:]:
        v11 = len(v16)
        for v12 in range(v11):
            v13, v14, v15 = v16[v12]
            v16.append((v8 + v13, v9 + v14, v10 + v15))
    v16 = [(v8 * v3 - v9 * v2, v10) for v8, v9, v10 in v16]
    v7.sort()
    v16.sort()
    v17 = len(v16) - 1
    v18 = v6
    for v19, v10 in v7:
        while v19 + v16[v17][0] > 0 and v17 > 0:
            v17 -= 1
        while v19 + v16[v17][0] == 0 and v17 >= 0:
            v20 = v10 + v16[v17][1]
            if v20 and v20 < v18:
                v18 = v20
            v17 -= 1
        if v17 < 0:
            break
    if v18 == v6:
        print(-1)
    else:
        print(v18)
f6()
