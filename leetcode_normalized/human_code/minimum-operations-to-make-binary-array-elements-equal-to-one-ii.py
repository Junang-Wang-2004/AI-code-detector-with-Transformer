class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2 ^ v1 & 1:
                continue
            v1 += 1
        return v1
