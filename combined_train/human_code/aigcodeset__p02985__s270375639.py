import sys
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 18
v2 = 10 ** 9 + 7

def f1():
    return list(map(int, sys.stdin.readline().split()))

def f2():
    v1, v2 = f1()
    v3 = [[] for v4 in range(v1 + 1)]
    for v4 in range(v1 - 1):
        v5, v6 = f1()
        v3[v5].append(v6)
        v3[v6].append(v5)
    v7 = 1
    v8 = [v7]
    v9 = v2
    v10 = v8.append
    v11 = [0] * (v1 + 1)
    v11[v7] = 1
    while len(v8) != 0:
        v12 = 1
        v13 = v8.pop()
        if v13 == v7:
            v14 = v2 - 1
        else:
            v14 = v2 - 2
        for v4 in v3[v13]:
            if v11[v4] == 1:
                continue
            v11[v4] = 1
            v12 = v12 * v14 % v2
            v14 -= 1
            v10(v4)
        v9 = v9 * v12 % v2
    print(v9 % v2)
if __name__ == '__main__':
    f2()
