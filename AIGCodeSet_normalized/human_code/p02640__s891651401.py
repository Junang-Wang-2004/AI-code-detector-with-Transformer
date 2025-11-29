import sys
sys.setrecursionlimit(10 ** 7)
v1 = sys.stdin.readline

def f1():
    v1, v2 = map(int, v1().split())
    for v3 in range(v1 + 1):
        if 2 * v3 + 4 * (v1 - v3) == v2:
            print('Yes')
            return
    print('No')
if __name__ == '__main__':
    f1()
