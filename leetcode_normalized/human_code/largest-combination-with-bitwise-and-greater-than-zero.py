class C1(object):

    def largestCombination(self, a1):
        """
        """
        v1 = []
        v2, v3 = (1, max(a1))
        while v2 <= v3:
            v1.append(sum((x & v2 > 0 for v4 in a1)))
            v2 <<= 1
        return max(v1)
