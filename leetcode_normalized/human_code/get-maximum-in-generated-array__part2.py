class C1(object):

    def getMaximumGenerated(self, a1):
        """
        """
        if a1 == 0:
            return 0
        v1 = [0] * (a1 + 1)
        v1[1] = 1
        v2 = 1
        for v3 in range(2, a1 + 1):
            if v3 % 2 == 0:
                v1[v3] = v1[v3 // 2]
            else:
                v1[v3] = v1[v3 // 2] + v1[v3 // 2 + 1]
            v2 = max(v2, v1[v3])
        return v2
