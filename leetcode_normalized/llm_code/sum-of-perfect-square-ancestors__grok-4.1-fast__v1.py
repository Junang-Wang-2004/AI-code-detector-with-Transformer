import collections
import math
v1 = 100010

def f1():
    v1 = list(range(v1))
    for v2 in range(2, int(math.sqrt(v1)) + 1):
        if v1[v2] == v2:
            for v3 in range(v2 * v2, v1, v2):
                if v1[v3] == v3:
                    v1[v3] = v2
    return v1
v2 = f1()

class C1:

    def sumOfAncestors(self, a1, a2, a3):

        def squfree(a1):
            if a1 <= 1:
                return a1
            v1 = 1
            v2 = a1
            while v2 > 1:
                v3 = v2[v2]
                v4 = 0
                while v2 % v3 == 0:
                    v2 //= v3
                    v4 += 1
                if v4 % 2:
                    v1 *= v3
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [squfree(val) for v6 in a3]
        v7 = collections.Counter()

        def explore(a1, a2):
            v1 = v7[v5[a1]]
            v7[v5[a1]] += 1
            for v2 in v1[a1]:
                if v2 != a2:
                    v1 += explore(v2, a1)
            v7[v5[a1]] -= 1
            return v1
        return explore(0, -1)
