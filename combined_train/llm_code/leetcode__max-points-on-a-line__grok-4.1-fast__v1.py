import collections
import math

class C1(object):

    def __init__(self, a1=0, a2=0):
        self.x = a1
        self.y = a2

class C2(object):

    def maxPoints(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = 1
            v5 = collections.defaultdict(int)
            for v6 in range(v3 + 1, v1):
                v7 = a1[v3].x - a1[v6].x
                v8 = a1[v3].y - a1[v6].y
                if v7 == 0 and v8 == 0:
                    v4 += 1
                else:
                    v9 = math.gcd(abs(v7), abs(v8))
                    v7 //= v9
                    v8 //= v9
                    if v7 < 0 or (v7 == 0 and v8 < 0):
                        v7 = -v7
                        v8 = -v8
                    v5[v8, v7] += 1
            v10 = v4
            for v11 in v5.values():
                v10 = max(v10, v11 + v4)
            v2 = max(v2, v10)
        return v2
