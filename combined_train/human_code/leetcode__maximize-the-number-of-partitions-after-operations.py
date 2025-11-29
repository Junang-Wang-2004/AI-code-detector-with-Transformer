class C1(object):

    def maxPartitionsAfterOperations(self, a1, a2):
        """
        """

        def popcount(a1):
            a1 = (a1 & 1431655765) + (a1 >> 1 & 1431655765)
            a1 = (a1 & 858993459) + (a1 >> 2 & 858993459)
            a1 = (a1 & 252645135) + (a1 >> 4 & 252645135)
            a1 = (a1 & 16711935) + (a1 >> 8 & 16711935)
            a1 = (a1 & 65535) + (a1 >> 16 & 65535)
            return a1
        v1 = [0] * (len(a1) + 1)
        v2 = [0] * (len(a1) + 1)
        v3 = v4 = 0
        for v5 in range(len(a1)):
            v4 |= 1 << ord(a1[v5]) - ord('a')
            if popcount(v4) > a2:
                v3 += 1
                v4 = 1 << ord(a1[v5]) - ord('a')
            v1[v5 + 1] = v3
            v2[v5 + 1] = v4
        v6 = [0] * (len(a1) + 1)
        v7 = [0] * (len(a1) + 1)
        v3 = v4 = 0
        for v5 in reversed(range(len(a1))):
            v4 |= 1 << ord(a1[v5]) - ord('a')
            if popcount(v4) > a2:
                v3 += 1
                v4 = 1 << ord(a1[v5]) - ord('a')
            v6[v5] = v3
            v7[v5] = v4
        v8 = 0
        for v5 in range(len(a1)):
            v9 = v1[v5] + v6[v5 + 1]
            v4 = v2[v5] | v7[v5 + 1]
            if popcount(v2[v5]) == popcount(v7[v5 + 1]) == a2 and popcount(v4) != 26:
                v9 += 3
            elif popcount(v4) + int(popcount(v4) != 26) > a2:
                v9 += 2
            else:
                v9 += 1
            v8 = max(v8, v9)
        return v8
