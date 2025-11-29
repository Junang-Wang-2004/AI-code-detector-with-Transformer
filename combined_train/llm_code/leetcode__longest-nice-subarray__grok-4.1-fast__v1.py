class C1:

    def longestNiceSubarray(self, a1):
        v1 = 0
        v2 = 0
        v3 = [-1] * 32
        for v4 in range(len(a1)):
            v5 = -1
            v6 = a1[v4]
            v7 = 0
            while 1 << v7 <= v6:
                if v6 & 1 << v7:
                    v5 = max(v5, v3[v7])
                v7 += 1
            v2 = max(v2, v5 + 1)
            v7 = 0
            while 1 << v7 <= v6:
                if v6 & 1 << v7:
                    v3[v7] = v4
                v7 += 1
            v1 = max(v1, v4 - v2 + 1)
        return v1
