class C1(object):

    def maxDifference(self, a1, a2):
        """
        """

        def diff(a1, a2):
            v1, v2, v3 = ([0] * (len(a1) + 1), [0] * (len(a1) + 1), [0] * (len(a1) + 1))
            for v4 in range(len(a1)):
                v1[v4 + 1] = v1[v4] + int(a1[v4] == a1)
                v2[v4 + 1] = v2[v4] + int(a1[v4] == a2)
                v3[v4 + 1] = v3[v4] + (int(a1[v4] == a1) - int(a1[v4] == a2))
            v5 = float('-inf')
            v6 = [[float('inf')] * 2 for v7 in range(2)]
            v8 = 0
            for v9 in range(a2 - 1, len(a1)):
                while a2 <= v9 - v8 + 1 and v1[v9 + 1] - v1[v8] and v2[v9 + 1] - v2[v8]:
                    v4, v10 = (v1[v8] % 2, v2[v8] % 2)
                    v6[v4][v10] = min(v6[v4][v10], v3[v8])
                    v8 += 1
                v4, v10 = (v1[v9 + 1] % 2, v2[v9 + 1] % 2)
                v5 = max(v5, v3[v9 + 1] - v6[v4 ^ 1][v10])
            return v5
        v1 = set(a1)
        return max((diff(x, y) for v2 in v1 for v3 in v1 if v2 != v3))
