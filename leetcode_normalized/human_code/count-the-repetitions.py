class C1(object):

    def getMaxRepetitions(self, a1, a2, a3, a4):
        """
        """
        v1 = [0] * (len(a3) + 1)
        v2 = {}
        v3, v4 = (0, 0)
        for v5 in range(1, a2 + 1):
            for v6 in range(len(a1)):
                if a1[v6] == a3[v3]:
                    v3 = (v3 + 1) % len(a3)
                    v4 += v3 == 0
            if v3 in v2:
                v6 = v2[v3]
                v7 = v1[v6]
                v8 = (v4 - v1[v6]) * ((a2 - v6) // (v5 - v6))
                v9 = v1[v6 + (a2 - v6) % (v5 - v6)] - v1[v6]
                return (v7 + v8 + v9) / a4
            v2[v3] = v5
            v1[v5] = v4
        return v1[a2] / a4
