class C1(object):

    def coinChange(self, a1, a2):
        """
        """
        v1 = 2147483647
        v2 = [v1] * (a2 + 1)
        v2[0] = 0
        for v3 in range(a2 + 1):
            if v2[v3] != v1:
                for v4 in a1:
                    if v3 + v4 <= a2:
                        v2[v3 + v4] = min(v2[v3 + v4], v2[v3] + 1)
        return v2[a2] if v2[a2] != v1 else -1
