import sys
sys.setrecursionlimit(300000)

def f1(a1: int, a2: int, a3: int, a4: 'List[int]', a5: 'List[int]'):
    a2 -= 1
    a3 -= 1
    v3 = [[] for v4 in range(a1)]
    for v5 in range(a1 - 1):
        v3[a4[v5] - 1].append(a5[v5] - 1)
        v3[a5[v5] - 1].append(a4[v5] - 1)
    v6 = [True] * a1

    def find_v(a1, a2, a3):
        a3[a1] = True
        if a1 == a3:
            v6[a1] = False
            return (a2, -1)
        v1 = 0
        v2 = -1
        for v3 in v3[a1]:
            if not a3[v3]:
                v1, v2 = find_v(v3, a2 + 1, a3)
                if v1 > 0:
                    if a2 >= v1 / 2:
                        v6[a1] = False
                    if a2 < v1 / 2 and v2 == -1:
                        v2 = a1
                    break
        return (v1, v2)
    v7 = [False] * a1
    v8, v9 = find_v(a2, 0, v7)

    def dfs(a1, a2, a3):
        a3[a1] = True
        v1 = a2
        for v2 in v3[a1]:
            if not a3[v2] and v6[v2]:
                v3 = dfs(v2, a2 + 1, a3)
                v1 = max(v1, v3)
        return v1
    v7 = [False] * a1
    v10 = dfs(v9, 0, v7)
    v10 += v8 // 2
    print(v10)
    return

def f4():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = int(next(v1))
    v5 = [int()] * (v2 - 1)
    v6 = [int()] * (v2 - 1)
    for v7 in range(v2 - 1):
        v5[v7] = int(next(v1))
        v6[v7] = int(next(v1))
    f1(v2, v3, v4, v5, v6)
if __name__ == '__main__':
    f4()
