import collections

class C1(object):

    def __init__(self, a1=0, a2=0):
        self.x = a1
        self.y = a2

class C2(object):

    def maxPoints(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in enumerate(a1):
            v4, v5 = (collections.defaultdict(int), 1)
            for v6 in range(v2 + 1, len(a1)):
                v7 = a1[v6]
                if v3.x == v7.x and v3.y == v7.y:
                    v5 += 1
                else:
                    v8 = float('inf')
                    if v3.x - v7.x != 0:
                        v8 = (v3.y - v7.y) * 1.0 / (v3.x - v7.x)
                    v4[v8] += 1
            v9 = v5
            for v8 in v4:
                v9 = max(v9, v4[v8] + v5)
            v1 = max(v1, v9)
        return v1
