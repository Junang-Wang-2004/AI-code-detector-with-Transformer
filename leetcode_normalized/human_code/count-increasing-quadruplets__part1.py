class C1(object):

    def countQuadruplets(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = 0
        for v3 in range(len(a1)):
            v4 = 0
            for v5 in range(v3):
                if a1[v5] < a1[v3]:
                    v4 += 1
                    v2 += v1[v5]
                elif a1[v5] > a1[v3]:
                    v1[v5] += v4
        return v2
