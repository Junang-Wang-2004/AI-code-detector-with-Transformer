class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v2 < v3:
                v2 = v3
                continue
            v2 += 1
            v1 += v2 - v3
        return v1
