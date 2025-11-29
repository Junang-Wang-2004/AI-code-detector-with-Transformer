class C1(object):

    def countSubmatrices(self, a1, a2):
        """
        """

        def count(a1):
            v1, v2 = ([0] * len(a1), [])
            for v3 in range(len(a1)):
                while v2 and a1[v2[-1]] >= a1[v3]:
                    v2.pop()
                v1[v3] = v1[v2[-1]] + a1[v3] * (v3 - v2[-1]) if v2 else a1[v3] * (v3 - -1)
                v2.append(v3)
            return sum(v1)
        v1 = 0
        v2 = [0] * len(a1)
        for v3 in reversed(list(range(len(a1[0])))):
            for v4 in range(len(a1)):
                v2[v4] = 0 if a1[v4][v3] > a2 else v2[v4] + 1 if v3 + 1 < len(a1[0]) and a1[v4][v3] >= a1[v4][v3 + 1] else 1
            v1 += count(v2)
        return v1
