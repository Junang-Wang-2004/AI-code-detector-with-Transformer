class C1(object):

    def palindromePartition(self, a1, a2):
        """
        """
        v1 = [[0] * len(a1) for v2 in range(len(a1))]
        for v3 in range(1, len(a1) + 1):
            for v4 in range(len(a1) - v3 + 1):
                v5 = v4 + v3 - 1
                if v4 == v5 - 1:
                    v1[v4][v5] = 0 if a1[v4] == a1[v5] else 1
                elif v4 != v5:
                    v1[v4][v5] = v1[v4 + 1][v5 - 1] if a1[v4] == a1[v5] else v1[v4 + 1][v5 - 1] + 1
        v6 = [[float('inf')] * len(a1) for v2 in range(2)]
        v6[1] = v1[0][:]
        for v7 in range(2, a2 + 1):
            v6[v7 % 2] = [float('inf')] * len(a1)
            for v4 in range(v7 - 1, len(a1)):
                for v5 in range(v7 - 2, v4):
                    v6[v7 % 2][v4] = min(v6[v7 % 2][v4], v6[(v7 - 1) % 2][v5] + v1[v5 + 1][v4])
        return v6[a2 % 2][len(a1) - 1]
