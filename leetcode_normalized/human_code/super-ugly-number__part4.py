class C1(object):

    def nthSuperUglyNumber(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v1[0] = 1
        v2 = list(a2)
        v3 = [0] * len(a2)
        for v4 in range(1, a1):
            v1[v4] = min(v2)
            for v5 in range(len(a2)):
                if v1[v4] == v2[v5]:
                    v3[v5] += 1
                    v2[v5] = a2[v5] * v1[v3[v5]]
        return v1[-1]
