import sys
sys.setrecursionlimit(1 << 25)
v1 = sys.stdin.readline
v2 = range
v3 = enumerate

def f1(*a1, **a2):
    print(*a1, **a2)
    sys.exit()

def f2(*a1, a2=1):
    return list(map(lambda x: x - a2, a1))

def f3():
    return int(v1())

def f4(a1):
    """H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合"""
    v1 = []
    for v2 in range(a1):
        v1.append(list(map(int, v1().split())))
    return tuple(map(list, zip(*v1)))
from collections import Counter
v4 = f3()
v5, = f4(v4)
v6 = 0
for v7 in Counter(v5).values():
    v6 += v7 & 1
print(v6)
