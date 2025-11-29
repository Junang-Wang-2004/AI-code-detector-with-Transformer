import sys, math, bisect
sys.setrecursionlimit(300000)

def f1(a1: int, a2: int, a3: int, a4: 'List[int]', a5: 'List[int]'):
    v1 = []
    for v2 in range(a1):
        v1.append([a4[v2], a5[v2]])
    v1.sort()
    v3 = 0
    v4 = []
    v5 = []
    v6 = 0
    v7 = 0
    v8 = 0
    for v2 in range(a1):
        v9 = v3
        while v8 < v2 and v4[v8] < v2:
            v7 = v5[v8]
            v8 += 1
        v9 -= v7
        v1[v2][1] = max(0, v1[v2][1] - v9 * a3)
        v10 = math.ceil(v1[v2][1] // a3)
        v3 += v10
        v11 = v1[v2][0] + a2
        while v6 < a1 and v1[v6][0] <= v11 + a2:
            v6 += 1
        v6 -= 1
        v4.append(v6)
        v5.append(v3)
    print(v3)
    return

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = int(next(v1))
    v5 = [int()] * v2
    v6 = [int()] * v2
    for v7 in range(v2):
        v5[v7] = int(next(v1))
        v6[v7] = int(next(v1))
    f1(v2, v3, v4, v5, v6)
if __name__ == '__main__':
    f2()
