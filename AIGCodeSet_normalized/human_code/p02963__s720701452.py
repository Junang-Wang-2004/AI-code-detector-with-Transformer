import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)
v4 = 1000000007

def f1(a1, a2):
    if a1 > a2:
        return a1
    else:
        return a2

def f2(a1, a2):
    if a1 < a2:
        return a1
    else:
        return a2

def f3():
    v1 = int(v2())
    if v1 != 10 ** 18:
        v2 = v1 % 1000000000
        v3 = v1 // 1000000000
        v4 = 1000000000
        v5 = v3
        v6 = v2
        v7 = -1
        print(0, 1, v4, 1 + v7, v6, 1 + v5)
    else:
        print(0, 0, 1000000000, 0, 0, 1000000000)
if __name__ == '__main__':
    f3()
