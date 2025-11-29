class C1(object):

    def specialArray(self, a1):
        """
        """
        v1 = 1000
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            v2[v3] += 1
        v4 = len(a1)
        for v5 in range(len(v2)):
            if v5 == v4:
                return v5
            v4 -= v2[v5]
        return -1
