class C1(object):

    def minSwaps(self, a1):
        """
        """

        def cost(a1, a2):
            v1 = 0
            for v2 in a1:
                v1 += int(v2) != a2
                a2 ^= 1
            return v1 // 2
        v1 = a1.count('1')
        v2 = len(a1) - v1
        if abs(v1 - v2) > 1:
            return -1
        if v1 > v2:
            return cost(a1, 1)
        if v1 < v2:
            return cost(a1, 0)
        return min(cost(a1, 1), cost(a1, 0))
