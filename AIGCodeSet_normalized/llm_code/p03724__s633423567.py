import sys
from collections import defaultdict

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return int(f1())

def f3():
    return list(map(int, f1().split()))

def f4():
    v1, v2 = f3()
    v3 = defaultdict(list)
    for v4 in range(v2):
        v5, v6 = f3()
        v3[v5].append(v6)
        v3[v6].append(v5)

    def dfs(a1, a2, a3):
        nonlocal is_possible
        for v1 in v3[a1]:
            if v1 == a2:
                continue
            if a3[v1] != -1:
                if (a3[a1] - a3[v1]) % 2 == 0:
                    v2 = False
                continue
            a3[v1] = a3[a1] + 1
            dfs(v1, a1, a3)
    v7 = True
    v8 = [-1] * (v1 + 1)
    v8[1] = 0
    dfs(1, 0, v8)
    if v7:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    f4()
