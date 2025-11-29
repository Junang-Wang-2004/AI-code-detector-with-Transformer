class C1(object):

    def minUnlockedIndices(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            if v2 < a1[v4]:
                v2 = a1[v4]
                v3 = 0
            elif v2 > a1[v4]:
                if v2 != a1[v4] + 1:
                    return -1
                v1 += v3
                v3 = 0
            v3 += a2[v4]
        return v1
