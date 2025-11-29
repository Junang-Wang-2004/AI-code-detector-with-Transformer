import sys

def f1():
    return sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 9)

def f2():
    v1, v2, v3 = map(int, f1().split())
    v4 = [v3 // v2 for v5 in range(v2)]
    for v6 in range(v2):
        v4[v6] += v6 * (v3 % v2)
    v7 = [v3 + 1 for v5 in range(v1 - v2)]
    v8 = v4 + v7
    print(*v8, sep=' ')
if __name__ == '__main__':
    f2()
