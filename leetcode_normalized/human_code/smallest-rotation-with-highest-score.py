class C1(object):

    def bestRotation(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [1] * v1
        for v3 in range(v1):
            v2[(v3 - a1[v3] + 1) % v1] -= 1
        for v3 in range(1, v1):
            v2[v3] += v2[v3 - 1]
        return v2.index(max(v2))
