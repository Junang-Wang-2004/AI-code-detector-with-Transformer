import sys

def f1():

    def dfs(a1, a2, a3, a4, a5):
        if a1 == a2:
            if a4 == 0:
                return
            if a3 not in a5:
                a5[a3] = a4
            else:
                a5[a3] = min(a5[a3], a4)
            return
        v1, v2, v3 = table[a1]
        dfs(a1 + 1, a2, a3 + v2 * Ma - v1 * Mb, a4 + v3, a5)
        dfs(a1 + 1, a2, a3, a4, a5)
    v1, v2, v3 = map(int, input().split())
    v4 = [tuple(map(int, input().split())) for v5 in range(v1)]
    v6, v7 = (dict(), dict())
    dfs(0, v1 // 2, 0, 0, v6)
    dfs(v1 // 2, v1, 0, 0, v7)
    v8 = 100 * 40 + 1
    v9 = v8
    if 0 in v6:
        v9 = min(v9, v6[0])
    if 0 in v7:
        v9 = min(v9, v7[0])
    for v10, v11 in v6.items():
        if -v10 in v7:
            v12 = v11 + v7[-v10]
            v9 = min(v9, v12)
    if v9 < v8:
        print(v9)
    else:
        print(-1)

def f3(a1, a2):
    for v1, v2 in a2.items():
        if a1 is v2:
            print('DEBUG:{} -> {}'.format(v1, v2), file=sys.stderr)
            return None
if __name__ == '__main__':
    f1()
