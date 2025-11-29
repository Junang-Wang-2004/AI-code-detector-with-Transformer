class C1(object):

    def findPermutation(self, a1):
        """
        """
        v1 = float('inf')
        v2 = len(a1)
        v3 = [[(v1, -1) for v4 in range(v2 - 1)] for v4 in range(1 << v2 - 1)]
        for v5 in range(v2 - 1):
            v3[1 << v5][v5] = (abs(v5 + 1 - a1[0]), -1)
        for v6 in range(1 << v2 - 1):
            for v5 in range(v2 - 1):
                if v6 & 1 << v5 == 0:
                    continue
                for v7 in range(v2 - 1):
                    if v7 == v5 or v6 & 1 << v7 == 0:
                        continue
                    v3[v6][v5] = min(v3[v6][v5], (v3[v6 ^ 1 << v5][v7][0] + abs(v5 + 1 - a1[v7 + 1]), v7))
        v4, v5 = min(((v3[-1][v5][0] + abs(0 - a1[v5 + 1]), v5) for v5 in range(v2 - 1)))
        v8 = [0]
        v6 = (1 << v2 - 1) - 1
        while v5 != -1:
            v8.append(v5 + 1)
            v6, v5 = (v6 ^ 1 << v5, v3[v6][v5][1])
        return v8
