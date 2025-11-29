import sys
input = sys.stdin.readline

def f1():
    return input().rstrip()

def f2():
    return int(input())

def f3():
    return map(int, input().split())

def f4(a1):
    v1 = 0
    for v2 in a1:
        v1 ^= v2
    return v1
v1 = f2()
v2 = list(f3())
v3 = []
for v4 in range(v1):
    v5 = 0
    for v6, v7 in enumerate(v2):
        if v4 != v6:
            v5 ^= v7
    v3.append(str(v5))
print(' '.join(v3))
