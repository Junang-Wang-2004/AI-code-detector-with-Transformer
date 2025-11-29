class C1(object):

    def maximumEvenSplit(self, a1):
        if a1 % 2 != 0:
            return []
        v1 = 0
        while v1 * (v1 + 1) <= a1:
            v1 += 1
        v1 -= 1
        if v1 == 0:
            return []
        v2 = []
        v3 = 0
        for v4 in range(1, v1):
            v5 = 2 * v4
            v2.append(v5)
            v3 += v5
        v6 = a1 - v3
        v2.append(v6)
        return v2
