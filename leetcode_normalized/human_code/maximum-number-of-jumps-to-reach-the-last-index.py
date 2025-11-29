class C1(object):

    def maximumJumps(self, a1, a2):
        """
        """
        v1 = [-1] * len(a1)
        v1[0] = 0
        for v2 in range(1, len(a1)):
            for v3 in range(v2):
                if abs(a1[v2] - a1[v3]) <= a2:
                    if v1[v3] != -1:
                        v1[v2] = max(v1[v2], v1[v3] + 1)
        return v1[-1]
