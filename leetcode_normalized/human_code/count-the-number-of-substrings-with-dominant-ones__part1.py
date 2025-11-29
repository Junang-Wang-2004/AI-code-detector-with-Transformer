class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1 = 0
        v2 = [-1] + [i for v3, v4 in enumerate(a1) if v4 == '0'] + [len(a1)]
        v5 = 1
        for v3 in range(len(a1)):
            if v2[v5] == v3:
                v5 += 1
            for v6 in range(min(int((-1 + (1 + 4 * (v3 + 1)) ** 0.5) / 2) + 1, v5)):
                if v6 ** 2 <= v3 - v2[v5 - v6 - 1] - v6:
                    v1 += min(min(v2[v5 - v6], v3) - v2[v5 - v6 - 1], v3 - v2[v5 - v6 - 1] - v6 - v6 ** 2 + 1)
        return v1
