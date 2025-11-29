class C1(object):

    def sameEndSubstringCount(self, a1, a2):
        """
        """
        v1 = [[0] * 26]
        for v2 in range(len(a1)):
            v1.append(v1[-1][:])
            v1[-1][ord(a1[v2]) - ord('a')] += 1
        v3 = [0] * len(a2)
        for v2, (v4, v5) in enumerate(a2):
            for v6 in range(26):
                v7 = v1[v5 + 1][v6] - v1[v4][v6]
                v3[v2] += (1 + v7) * v7 // 2
        return v3
