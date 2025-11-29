class C1(object):

    def longestPalindromeSubseq(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        for v3 in range(v1):
            v2[v3] = 1
        for v4 in range(v1 - 2, -1, -1):
            v5 = 0
            for v6 in range(v4 + 1, v1):
                v7 = v2[v6]
                if a1[v4] == a1[v6]:
                    v2[v6] = v5 + 2
                else:
                    v2[v6] = max(v2[v6], v2[v6 - 1])
                v5 = v7
        return v2[v1 - 1]
