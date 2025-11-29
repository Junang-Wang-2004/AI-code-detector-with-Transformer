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

def f8():
    v1, v2 = f3()
    v3 = (v1 - 1) * (v1 - 2) // 2 - v2
    if v3 < 0:
        print(-1)
        exit()
    v4 = []
    for v5 in range(1, v1):
        v4.append([v5, v1])
    for v5 in range(1, v1):
        for v6 in range(v5 + 1, v1):
            if v3 > 0:
                v3 -= 1
                v4.append([v5, v6])
    print(len(v4))
    for v5, v6 in v4:
        print(v5, v6)
if __name__ == '__main__':
    f8()
