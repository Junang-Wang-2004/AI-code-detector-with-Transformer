class C1(object):

    def numMovesStonesII(self, a1):
        """
        """
        a1.sort()
        v1, v2 = (0, float('inf'))
        v3 = max(a1[-1] - a1[1], a1[-2] - a1[0]) - (len(a1) - 2)
        for v4 in range(len(a1)):
            while a1[v4] - a1[v1] + 1 > len(a1):
                v1 += 1
            if len(a1) - (v4 - v1 + 1) == 1 and a1[v4] - a1[v1] + 1 == len(a1) - 1:
                v2 = min(v2, 2)
            else:
                v2 = min(v2, len(a1) - (v4 - v1 + 1))
        return [v2, v3]
