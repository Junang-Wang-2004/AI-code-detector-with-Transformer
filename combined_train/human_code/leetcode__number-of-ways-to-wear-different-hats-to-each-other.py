class C1(object):

    def numberWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 40
        v3 = [[] for v4 in range(v2)]
        for v5 in range(len(a1)):
            for v6 in a1[v5]:
                v3[v6 - 1].append(v5)
        v7 = [0] * (1 << len(a1))
        v7[0] = 1
        for v8 in v3:
            for v9 in reversed(range(len(v7))):
                for v10 in v8:
                    if v9 & 1 << v10:
                        continue
                    v7[v9 | 1 << v10] += v7[v9]
                    v7[v9 | 1 << v10] %= v1
        return v7[-1]
