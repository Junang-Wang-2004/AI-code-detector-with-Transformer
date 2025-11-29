import sys, queue, math, copy, itertools, bisect, collections, heapq

def f1():
    sys.setrecursionlimit(10 ** 7)
    v1 = 10 ** 6
    v2 = 10 ** 9 + 7
    v3 = lambda: [int(x) for v4 in sys.stdin.readline().split()]
    v5 = lambda: int(sys.stdin.readline())
    v6 = lambda: sys.stdin.readline().rstrip()
    v7, v8 = v3()
    v9 = [[] for v10 in range(v7)]
    v11 = [[v1, v1, v1] for v10 in range(v7)]
    for v10 in range(v8):
        v12, v13 = v3()
        v9[v12 - 1].append(v13 - 1)
    v14, v15 = v3()
    v14 -= 1
    v15 -= 1
    v16 = collections.deque()
    v16.append((v14, 0, 0))
    v11[v14][0] = 0
    while v16:
        v17, v18, v19 = v16.popleft()
        v20 = (v18 + 1) % 3
        for v21 in v9[v17]:
            if v11[v21][v20] > v19 + 1:
                v11[v21][v20] = v19 + 1
                v16.append((v21, v20, v19 + 1))
    if v11[v15][0] < v1:
        print(v11[v15][0] // 3)
    else:
        print(-1)
if __name__ == '__main__':
    f1()
