import sys
import math

def f1():
    return sys.stdin.readline().strip()
v1 = 10 ** 9 + 7
sys.setrecursionlimit(20000000)

def f2():
    v1 = int(f1())
    v2 = list(map(int, f1().split()))
    v2.sort()
    v3 = v2[0]
    v4 = set()
    for v5 in range(1, v1):
        v6 = math.gcd(v2[v5], v3)
        if v6 == 1:
            v4.add(1)
        elif v6 == v3:
            continue
        else:
            v4.add(v6)
    if len(v4) == 0:
        print(v3)
    else:
        print(min(v4))
if __name__ == '__main__':
    f2()
