class C1(object):

    def maxRemovals(self, a1, a2, a3):
        """
        """
        v1 = [float('-inf')] * (len(a2) + 1)
        v1[0] = 0
        v2 = [False] * len(a1)
        for v3 in a3:
            v2[v3] = True
        for v4 in range(len(a1)):
            for v5 in reversed(range(len(a2) + 1)):
                v1[v5] += v2[v4]
                if v5 - 1 >= 0 and a2[v5 - 1] == a1[v4]:
                    v1[v5] = max(v1[v5], v1[v5 - 1])
        return v1[-1]
