class C1(object):

    def stringCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4, v5 = [1 << i for v6 in range(4)]
        v7 = [0] * (1 << 4)
        v7[0] = 1
        for v8 in range(a1):
            v9 = [0] * (1 << 4)
            for v10 in range(len(v7)):
                v9[v10 | v2] = (v9[v10 | v2] + v7[v10]) % v1
                if not v10 & v3:
                    v9[v10 | v3] = (v9[v10 | v3] + v7[v10]) % v1
                else:
                    v9[v10 | v4] = (v9[v10 | v4] + v7[v10]) % v1
                v9[v10 | v5] = (v9[v10 | v5] + v7[v10]) % v1
                v9[v10] = (v9[v10] + 23 * v7[v10]) % v1
            v7 = v9
        return v7[-1]
