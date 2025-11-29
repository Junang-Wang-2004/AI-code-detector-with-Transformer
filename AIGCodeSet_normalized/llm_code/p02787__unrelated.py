import sys

def f1():
    v1, v2 = map(int, sys.stdin.readline().split())
    v3 = [list(map(int, sys.stdin.readline().split())) for v4 in range(v2)]
    v3.sort(key=lambda x: -x[0] / x[1])
    v5 = 0
    for v6, v7 in v3:
        v8 = min(v1, v7) // v7
        v1 -= v8 * v6
        v5 += v8 * v7
        if v1 <= 0:
            break
    print(v5)
if __name__ == '__main__':
    f1()
