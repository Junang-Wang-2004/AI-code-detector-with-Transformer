class C1(object):

    def waysToMakeFair(self, a1):
        """
        """
        v1 = [0] * 2
        v2 = [sum((a1[i] for v3 in range(k, len(a1), 2))) for v4 in range(2)]
        v5 = 0
        for v3, v6 in enumerate(a1):
            v2[v3 % 2] -= v6
            v5 += int(v1[0] + v2[1] == v1[1] + v2[0])
            v1[v3 % 2] += v6
        return v5
