import sys

def f1():
    return sys.stdin.readline().rstrip()
from operator import itemgetter

def f2():
    v1 = int(f1())
    v2 = [[] for v3 in range(v1)]
    v4 = [tuple(map(int, f1().split())) for v5 in range(v1 - 1)]
    for v6, v7 in v4:
        v2[v6 - 1].append(v7 - 1)
        v2[v7 - 1].append(v6 - 1)
    v8 = list(map(int, f1().split()))
    v8.sort(reverse=True)
    v9 = [[v5, 0, 0] for v5 in range(v1)]
    for v5, v10 in enumerate(v2):
        v9[v5][1] = len(v10)
    v9.sort(key=itemgetter(1), reverse=True)
    for v5 in range(v1):
        v9[v5][2] = v8[v5]
    v9.sort(key=itemgetter(0))
    v11 = 0
    for v5 in range(v1 - 1):
        v6, v7 = v4[v5]
        v11 += min(v9[v6 - 1][2], v9[v7 - 1][2])
    print(v11)
    print(' '.join(map(str, [x[2] for v12 in v9])))
if __name__ == '__main__':
    f2()
