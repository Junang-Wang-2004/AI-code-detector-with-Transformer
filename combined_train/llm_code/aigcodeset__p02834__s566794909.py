import sys

def f1(a1: int, a2: int, a3: int, a4: 'List[int]', a5: 'List[int]'):
    if a2 == a3:
        return 0
    v1 = [[] for v2 in range(a1)]
    for v3, v4 in zip(a4, a5):
        v1[v3 - 1].append(v4 - 1)
        v1[v4 - 1].append(v3 - 1)
    v5 = [[float('inf')] * a1 for v2 in range(2)]

    def dfs(a1, a2, a3):
        if v5[a3][a1] < float('inf'):
            return
        v5[a3][a1] = a2
        for v1 in v1[a1]:
            dfs(v1, a2 + 1, a3)
    dfs(a2 - 1, 0, 0)
    dfs(a3 - 1, 0, 1)
    v6 = max((v3 for v7, v3 in zip(*v5) if v7 < v3))
    return v6 - 1

def f3():

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
    print(f1(v2, v3, v4, v5, v6))

def f5():
    import doctest
    doctest.testmod()
if __name__ == '__main__':
    f3()
