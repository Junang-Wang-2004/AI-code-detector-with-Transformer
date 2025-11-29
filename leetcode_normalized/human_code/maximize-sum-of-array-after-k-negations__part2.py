class C1(object):

    def largestSumAfterKNegations(self, a1, a2):
        """
        """
        a1.sort()
        v1 = a2
        for v2 in range(a2):
            if a1[v2] >= 0:
                break
            a1[v2] = -a1[v2]
            v1 -= 1
        return sum(a1) - v1 % 2 * min(a1) * 2
