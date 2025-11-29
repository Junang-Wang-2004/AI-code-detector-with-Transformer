class C1(object):

    def numWays(self, a1, a2):
        """
        """
        if a1 == 0:
            return 0
        elif a1 == 1:
            return a2
        v1 = [0] * a1
        v1[0] = a2
        v1[1] = (a2 - 1) * v1[0] + a2
        for v2 in range(2, a1):
            v1[v2] = (a2 - 1) * (v1[v2 - 1] + v1[v2 - 2])
        return v1[a1 - 1]
