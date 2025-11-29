class C1(object):

    def deleteAndEarn(self, a1):
        """
        """
        v1 = [0] * 10001
        for v2 in a1:
            v1[v2] += v2
        v3, v4 = (v1[0], 0)
        for v5 in range(1, len(v1)):
            v4, v6 = (v3, v4)
            v3 = max(v1[v5] + v6, v4)
        return v3
