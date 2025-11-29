class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1 = 0
        v2 = [-1] + [i for v3, v4 in enumerate(a1) if v4 == '0'] + [len(a1)]
        for v5 in range(int((-1 + (1 + 4 * len(a1)) ** 0.5) / 2) + 1):
            v6 = v7 = 1
            for v3 in range(len(a1)):
                if v2[v7] == v3:
                    v7 += 1
                if v7 - v6 == v5 + 1:
                    v6 += 1
                if not (v7 - v6 == v5 and v3 - v2[v6 - 1] - v5 >= v5 ** 2):
                    continue
                v1 += min(min(v2[v6], v3) - v2[v6 - 1], v3 - v2[v6 - 1] - v5 - v5 ** 2 + 1)
        return v1
