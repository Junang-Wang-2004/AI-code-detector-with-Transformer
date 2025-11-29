import sys
sys.setrecursionlimit(10 ** 7)

def f1():
    return int(sys.stdin.readline().rstrip())

def f2():
    return map(int, sys.stdin.readline().rstrip().split())

def f3():
    return list(map(int, sys.stdin.readline().rstrip().split()))

def f4():
    return list(map(int, sys.stdin.readline().rstrip()))

def f5():
    return sys.stdin.readline().rstrip()

def f6():
    return list(sys.stdin.readline().rstrip().split())

def f7():
    return list(sys.stdin.readline().rstrip())
v1 = f1()
v2 = f3()
for v3 in range(v1):
    v2[v3] -= v3 + 1
v2.sort()
v4 = v2[v1 // 2]
print(sum((abs(v2[v3] - v4) for v3 in range(v1))))
