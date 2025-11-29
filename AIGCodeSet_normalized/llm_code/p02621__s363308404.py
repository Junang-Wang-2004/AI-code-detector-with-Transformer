import sys

def f1():
    return list(map(int, sys.stdin.buffer.readline().split()))

def f2():
    return int(sys.stdin.buffer.readline())

def f3():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

def f4():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

def f5(a1):
    return [f2() for v1 in range(a1)]

def f6(a1):
    return [f1() for v1 in range(a1)]

def f7(a1):
    return [f4() for v1 in range(a1)]

def f8(a1):
    return [f3() for v1 in range(a1)]

def f9(a1):
    return [list(f4()) for v1 in range(a1)]

def f10(a1):
    return [[int(j) for v1 in list(f4())] for v2 in range(a1)]
v1 = 10 ** 9 + 7
v2 = f2()
v3 = v2 + v2 ** 2 + v2 ** 3
print(v3)
