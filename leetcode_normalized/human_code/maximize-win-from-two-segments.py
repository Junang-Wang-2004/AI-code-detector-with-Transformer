class C1(object):

    def maximizeWin(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        v2 = v3 = 0
        for v4 in range(len(a1)):
            while a1[v4] - a1[v3] > a2:
                v3 += 1
            v1[v4 + 1] = max(v1[v4], v4 - v3 + 1)
            v2 = max(v2, v1[v3] + (v4 - v3 + 1))
        return v2
