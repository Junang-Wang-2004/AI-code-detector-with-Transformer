import sys

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return int(sys.stdin.readline().rstrip())

def f3():
    return list(map(int, sys.stdin.readline().rstrip().split()))

def f4():
    return list(sys.stdin.readline().rstrip().split())
v1 = 1000000000000
v2 = f2()
if v2 >= 400 and v2 < 600:
    v3 = 8
elif v2 < 800:
    v3 = 7
elif v2 < 1000:
    v3 = 6
elif v2 < 1200:
    v3 = 5
elif v2 < 1400:
    v3 = 4
elif v2 < 1600:
    v3 = 3
elif v2 < 1800:
    v3 = 2
else:
    v3 = 1
print(v3)
