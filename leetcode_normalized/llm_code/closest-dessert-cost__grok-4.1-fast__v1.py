class C1(object):

    def closestCost(self, a1, a2, a3):
        v1 = set(a1)
        for v2 in a2:
            v3 = set()
            for v4 in v1:
                v3.add(v4)
                v3.add(v4 + v2)
                v3.add(v4 + 2 * v2)
            v1 = v3
        return min(v1, key=lambda val: (abs(val - a3), val))
