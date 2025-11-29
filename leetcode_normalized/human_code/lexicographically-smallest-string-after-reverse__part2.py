class C1(object):

    def lexSmallest(self, a1):
        """
        """
        v1 = a1
        for v2 in range(2, len(a1) + 1):
            v1 = min(v1, a1[:v2][::-1] + a1[v2:], a1[:-v2] + a1[-v2:][::-1])
        return v1
