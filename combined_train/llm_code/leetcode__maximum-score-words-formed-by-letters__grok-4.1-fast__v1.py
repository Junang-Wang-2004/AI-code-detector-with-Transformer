class C1:

    def maxScoreWords(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [[0] * 26 for v3 in range(v1)]
        v4 = [0] * v1
        for v5 in range(v1):
            for v6 in a1[v5]:
                v7 = ord(v6) - ord('a')
                v2[v5][v7] += 1
                v4[v5] += a3[v7]
        v8 = [0] * 26
        for v6 in a2:
            v8[ord(v6) - ord('a')] += 1
        self.ans = 0

        def search(a1, a2, a3):
            self.ans = max(self.ans, a2)
            if a1 == v1:
                return
            search(a1 + 1, a2, a3)
            v1 = v2[a1]
            if all((a3[k] >= v1[k] for v2 in range(26))):
                for v2 in range(26):
                    a3[v2] -= v1[v2]
                search(a1 + 1, a2 + v4[a1], a3)
                for v2 in range(26):
                    a3[v2] += v1[v2]
        search(0, 0, v8)
        return self.ans
