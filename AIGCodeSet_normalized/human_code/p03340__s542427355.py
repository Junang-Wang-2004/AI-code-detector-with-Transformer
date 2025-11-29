from copy import deepcopy
from operator import add, sub

class C1:

    def __init__(self, a1, a2=0, a3=add, a4=sub):
        self.cond = a1
        self.init = a2
        self.next_right = a3
        self.next_left = a4

    def __call__(self, a1, a2=True):
        v1 = self.cond
        v2, v3 = (self.next_right, self.next_left)
        v4 = deepcopy(self.init)
        v5 = len(a1)
        v6 = {}
        v7 = 0
        for v8 in range(v5):
            if not a2:
                v6[v8] = v7
            while v7 < v5 and v1(v4, a1[v7]):
                v4 = v2(v4, a1[v7])
                v7 += 1
                v6[v8] = v7
            if v8 == v7:
                v7 += 1
            else:
                v4 = v3(v4, a1[v8]) if v8 + 1 != v7 else deepcopy(self.init)
        return list(v6.items())

    def maximum(self, a1):
        v1 = self.__call__(a1)
        return max((r - l for v2, v3 in v1)) if v1 else 0

    def count(self, a1):
        v1 = self.__call__(a1, False)
        return sum((r - l for v2, v3 in v1))
v1, *v2 = map(int, open(0).read().split())
print(C1(lambda s, n: s + v1 == s ^ v1).count(v2))
