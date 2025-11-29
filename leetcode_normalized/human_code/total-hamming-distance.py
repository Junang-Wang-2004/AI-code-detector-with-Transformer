class C1(object):

    def totalHammingDistance(self, a1):
        """
        """
        v1 = 0
        for v2 in range(32):
            v3 = [0] * 2
            for v4 in a1:
                v3[v4 >> v2 & 1] += 1
            v1 += v3[0] * v3[1]
        return v1
