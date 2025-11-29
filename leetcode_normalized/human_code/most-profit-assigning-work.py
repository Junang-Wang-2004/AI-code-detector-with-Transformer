class C1(object):

    def maxProfitAssignment(self, a1, a2, a3):
        """
        """
        v1 = list(zip(a1, a2))
        v1.sort()
        a3.sort()
        v2, v3, v4 = (0, 0, 0)
        for v5 in a3:
            while v3 < len(v1) and v1[v3][0] <= v5:
                v4 = max(v4, v1[v3][1])
                v3 += 1
            v2 += v4
        return v2
