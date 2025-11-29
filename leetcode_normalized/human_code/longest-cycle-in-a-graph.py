class C1(object):

    def longestCycle(self, a1):
        """
        """
        v1 = -1
        v2 = [-1] * len(a1)
        v3 = 0
        for v4 in range(len(a1)):
            if v2[v4] != -1:
                continue
            v5 = v3
            while v4 != -1:
                if v2[v4] != -1:
                    break
                v2[v4] = v3
                v3 += 1
                v4 = a1[v4]
            if v4 != -1 and v2[v4] >= v5:
                v1 = max(v1, v3 - v2[v4])
        return v1
