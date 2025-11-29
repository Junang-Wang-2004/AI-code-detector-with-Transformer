class C1(object):

    def maxCount(self, a1, a2, a3):
        """
        """
        v1 = set(a1)
        v2 = v3 = 0
        for v4 in range(1, a2 + 1):
            if v4 in v1:
                continue
            if v3 + v4 > a3:
                break
            v3 += v4
            v2 += 1
        return v2
