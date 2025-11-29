class C1(object):

    def getMaxLen(self, a1):
        """
        """
        v1, v2, v3, v4 = (0, 0, -1, -1)
        for v5 in range(len(a1)):
            if a1[v5] == 0:
                v2 = 0
                v3 = v5
                v4 = -1
                continue
            if a1[v5] < 0:
                if v4 == -1:
                    v4 = v5
                v2 += 1
            v1 = max(v1, v5 - (v3 if v2 % 2 == 0 else v4))
        return v1
