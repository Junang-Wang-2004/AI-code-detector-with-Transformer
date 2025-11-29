class C1(object):

    def findMaxConsecutiveOnes(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 = v2 + 1 if v3 else 0
            v1 = max(v1, v2)
        return v1
