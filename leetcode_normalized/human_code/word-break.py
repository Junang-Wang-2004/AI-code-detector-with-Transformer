class C1(object):

    def wordBreak(self, a1, a2):
        """
        """
        v1 = len(a1)
        v2 = 0
        for v3 in a2:
            v2 = max(v2, len(v3))
        v4 = [False for v5 in range(v1 + 1)]
        v4[0] = True
        for v6 in range(1, v1 + 1):
            for v7 in range(1, min(v6, v2) + 1):
                if v4[v6 - v7] and a1[v6 - v7:v6] in a2:
                    v4[v6] = True
                    break
        return v4[-1]
