class C1(object):

    def countDistinct(self, a1, a2, a3):
        """
        """
        v1, v2 = (10 ** 9 + 7, 200)
        v3 = 0
        v4, v5 = ([0] * len(a1), [0] * len(a1))
        for v6 in range(1, len(a1) + 1):
            v7 = set()
            for v8 in range(len(a1) - v6 + 1):
                v4[v8] += a1[v8 + v6 - 1] % a3 == 0
                if v4[v8] > a2:
                    continue
                v5[v8] = (v5[v8] * v2 + a1[v8 + v6 - 1]) % v1
                v7.add(v5[v8])
            v3 += len(v7)
        return v3
