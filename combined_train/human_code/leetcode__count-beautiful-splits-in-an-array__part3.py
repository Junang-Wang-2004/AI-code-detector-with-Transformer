class C1(object):

    def beautifulSplits(self, a1):
        """
        """

        def z_function(a1, a2, a3):
            v1 = [0] * (a3 - a2 + 1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1)):
                if v4 <= v3:
                    v1[v4] = min(v3 - v4 + 1, v1[v4 - v2])
                while v4 + v1[v4] < len(v1) and a1[a2 + v1[v4]] == a1[a2 + v4 + v1[v4]]:
                    v1[v4] += 1
                if v4 + v1[v4] - 1 > v3:
                    v2, v3 = (v4, v4 + v1[v4] - 1)
            return v1
        v1 = 0
        v2 = z_function(a1, 0, len(a1) - 1)
        for v3 in range(1, len(a1) - 1):
            v4 = z_function(a1, v3, len(a1) - 1)
            for v5 in range(v3 + 1, len(a1)):
                if v2[v3] >= v3 and v5 - v3 >= v3 or v4[v5 - v3] >= v5 - v3:
                    v1 += 1
        return v1
