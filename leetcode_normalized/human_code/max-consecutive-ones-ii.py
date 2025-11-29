class C1(object):

    def findMaxConsecutiveOnes(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        for v4 in a1:
            if v4 == 0:
                v1 = max(v1, v2 + v3 + 1)
                v2, v3 = (v3, 0)
            else:
                v3 += 1
        return min(max(v1, v2 + v3 + 1), len(a1))
