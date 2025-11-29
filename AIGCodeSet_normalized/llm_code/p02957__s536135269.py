import sys
v1 = sys.stdin
sys.setrecursionlimit(10 ** 7)

def f1():
    return map(int, v1.readline().split())

def f2():
    return map(lambda x: int(x) - 1, v1.readline().split())

def f3():
    return map(float, v1.readline().split())

def f4():
    return v1.readline().split()

def f5():
    return v1.readline().rstrip()

def f6():
    return list(f5())

def f7():
    return int(v1.readline())

def f8():
    return float(v1.readline())
v2, v3 = f1()
if (v2 + v3) % 2 == 1:
    print('IMPOSSIBLE')
else:
    v4 = (v2 + v3) // 2
    print(int(v4))
