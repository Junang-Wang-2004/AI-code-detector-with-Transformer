import sys

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

class C1:

    def __init__(self, a1, a2=0):
        self.s = [a2] * (a1 + 1)
        self.n = a1

    def add(self, a1, a2):
        while a2 < self.n + 1:
            self.s[a2] = self.s[a2] + a1
            a2 += a2 & -a2
        return

    def get(self, a1):
        v1 = 0
        while a1 > 0:
            v1 = v1 + self.s[a1]
            a1 -= a1 & -a1
        return v1
from collections import defaultdict

def f10():
    v1 = f2()
    v2 = input()
    v3 = [0] + list(v2)
    v4 = defaultdict(lambda: C1(v1))
    for v5, v6 in enumerate(v2):
        v4[v6].add(1, v5 + 1)
    v7 = f2()
    for v8 in range(v7):
        v9, v10, v11 = input().split()
        if int(v9) == 1:
            v10 = int(v10)
            v4[v3[v10]].add(0, v10)
            v4[v11].add(1, v10)
            v3[v10] = v11
        else:
            v10 = int(v10)
            v11 = int(v11)
            v12 = 0
            for v13 in v4.values():
                if v13.get(v11) - v13.get(v10 - 1) > 0:
                    v12 += 1
            print(v12)
if __name__ == '__main__':
    f10()
