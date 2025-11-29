class C1(object):

    def maxValueOfCoins(self, a1, a2):
        """
        """
        v1 = [0]
        for v2 in a1:
            v3 = [0] * min(len(v1) + len(v2), a2 + 1)
            for v4 in range(len(v1)):
                v5 = 0
                for v6 in range(min(a2 - v4, len(v2)) + 1):
                    v3[v4 + v6] = max(v3[v4 + v6], v1[v4] + v5)
                    v5 += v2[v6] if v6 < len(v2) else 0
            v1 = v3
        return v1[-1]
