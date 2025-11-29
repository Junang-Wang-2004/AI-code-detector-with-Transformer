class C1(object):

    def maximumEvenSplit(self, a1):
        """
        """
        if a1 % 2:
            return []
        v1 = []
        v2 = 2
        while v2 <= a1:
            v1.append(v2)
            a1 -= v2
            v2 += 2
        v1[-1] += a1
        return v1
