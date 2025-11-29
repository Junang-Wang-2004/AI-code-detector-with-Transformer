import sys
input = sys.stdin.buffer.readline

def f1():
    return sys.stdin.read()

def f2():
    return int(input())

def f3():
    return map(int, input().split())

def f4():
    return map(float, input().split())

def f5():
    return list(map(int, input().split()))

def f6():
    return list(map(float, input().split()))

def f7():
    return tuple(map(int, input().split()))
from collections import deque

def f8():
    v1, v2 = f3()
    v3 = []
    if v2 == 0:
        for v4 in range(2 ** v1):
            v3.append(v4)
            v3.append(v4)
        print(*v3)
        exit()
    if 2 ** v1 <= v2:
        print(-1)
        exit()
    v3.append(0)
    v3.append(v2)
    v3.append(0)
    for v4 in range(1, 2 ** v1):
        if v4 != v2:
            v3.append(v4)
    v3.append(v2)
    for v4 in reversed(range(1, 2 ** v1)):
        if v4 != v2:
            v3.append(v4)
    print(*v3)
if __name__ == '__main__':
    f8()
