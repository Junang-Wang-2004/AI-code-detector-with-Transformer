class C1(object):

    def baseUnitConversions(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(len(a1) + 1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
        v7 = [0] * len(v2)
        v7[0] = 1
        v8 = [0]
        while v8:
            v9 = []
            for v4 in v8:
                for v5, v6 in v2[v4]:
                    v7[v5] = v7[v4] * v6 % v1
                    v9.append(v5)
            v8 = v9
        return v7
