import sys
v1 = sys.stdin

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
from collections import Counter
v2 = f6()
v3 = Counter(v2)
v4 = v2[::-1]
v5 = Counter([])
v6 = 0
for v7 in v4:
    v8 = True
    v5[v7] += 1
    for v9 in v5.values():
        if v9 % 2 == 1:
            v8 = False
            break
    if v8:
        v6 = sum(v5.values())
        break
print(len(v2) - v6)
