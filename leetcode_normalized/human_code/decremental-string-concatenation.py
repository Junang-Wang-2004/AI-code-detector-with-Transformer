class C1(object):

    def minimizeConcatenatedLength(self, a1):
        """
        """
        v1 = [[float('-inf')] * 26 for v2 in range(2)]
        v1[0][ord(a1[0][-1]) - ord('a')] = v1[1][ord(a1[0][0]) - ord('a')] = 0
        for v3 in range(1, len(a1)):
            v4 = [[float('-inf')] * 26 for v2 in range(2)]
            for v5 in range(2):
                for v6 in range(26):
                    if v1[v5][v6] == float('-inf'):
                        continue
                    v7 = v6 if v5 else ord(a1[v3 - 1][0]) - ord('a')
                    v8 = v6 if not v5 else ord(a1[v3 - 1][-1]) - ord('a')
                    v4[0][v8] = max(v4[0][v8], v1[v5][v6] + int(ord(a1[v3][-1]) - ord('a') == v7))
                    v4[1][v7] = max(v4[1][v7], v1[v5][v6] + int(v8 == ord(a1[v3][0]) - ord('a')))
            v1 = v4
        return sum((len(w) for v9 in a1)) - max((v1[v5][v6] for v5 in range(2) for v6 in range(26)))
