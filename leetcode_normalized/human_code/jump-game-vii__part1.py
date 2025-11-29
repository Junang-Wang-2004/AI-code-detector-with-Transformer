class C1(object):

    def canReach(self, a1, a2, a3):
        """
        """
        v1 = [False] * len(a1)
        v1[0] = True
        v2 = 0
        for v3 in range(1, len(a1)):
            if v3 >= a2:
                v2 += v1[v3 - a2]
            if v3 > a3:
                v2 -= v1[v3 - a3 - 1]
            v1[v3] = v2 > 0 and a1[v3] == '0'
        return v1[-1]
