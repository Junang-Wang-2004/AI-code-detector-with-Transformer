class C1(object):

    def maxHammingDistances(self, a1, a2):
        """
        """
        v1 = []
        v2 = [-1] * (1 << a2)
        for v3 in a1:
            if v2[v3] != -1:
                continue
            v2[v3] = 0
            v1.append(v3)
        v4 = 0
        while v1:
            v4 += 1
            v5 = []
            for v6 in v1:
                for v7 in range(a2):
                    if v2[v6 ^ 1 << v7] != -1:
                        continue
                    v2[v6 ^ 1 << v7] = v4
                    v5.append(v6 ^ 1 << v7)
            v1 = v5
        return [a2 - v2[(1 << a2) - 1 ^ v3] for v3 in a1]
