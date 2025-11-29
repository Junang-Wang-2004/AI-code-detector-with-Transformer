import sys

def f1():
    return int(sys.stdin.buffer.readline())

def f2():
    return map(int, sys.stdin.buffer.readline().split())

def f3():
    return list(map(int, sys.stdin.buffer.readline().split()))
v1, v2 = f2()
v3 = [1] * v1
for v4 in range(v2):
    v5 = f1()
    v6 = f3()
    for v7 in v6:
        v3[v7 - 1] = 0
print(sum(v3))
