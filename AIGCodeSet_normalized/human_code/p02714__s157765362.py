import sys
import os
import math
v1 = lambda: int(sys.stdin.buffer.readline().rstrip())
v2 = lambda: list(map(int, sys.stdin.buffer.readline().split()))
v3 = lambda: list(map(float, sys.stdin.buffer.readline().split()))
v4 = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for v5 in range(n)]
v6 = lambda: sys.stdin.buffer.readline().decode().rstrip()
v7 = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
v8 = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for v5 in range(n)]
v9 = 10 ** 9 + 7

def f1():
    if os.getenv('LOCAL'):
        sys.stdin = open('input.txt', 'r')
    v1 = v1()
    v2 = v6()
    v3 = v2.count('R') * v2.count('G') * v2.count('B')
    for v4 in range(v1):
        for v5 in range(v4 + 1, v1):
            v6 = v5 + v5 - v4
            if v6 < v1:
                if v2[v4] != v2[v5] and v2[v4] != v2[v6] and (v2[v5] != v2[v6]):
                    v3 -= 1
    print(v3)
if __name__ == '__main__':
    f1()
