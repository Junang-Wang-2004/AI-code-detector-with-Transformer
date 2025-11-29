class C1(object):

    def hIndex(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            if v3 >= v1:
                v2[v1] += 1
            else:
                v2[v3] += 1
        v4 = 0
        for v5 in reversed(range(0, v1 + 1)):
            v4 += v2[v5]
            if v4 >= v5:
                return v5
        return v4
