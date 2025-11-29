class C1:

    def longestBalanced(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = [0] * 26
            v5 = 0
            v6 = 0
            v7 = 0
            v8 = v3
            while v8 < v1:
                v9 = ord(a1[v8]) - ord('a')
                if v4[v9] == 0:
                    v5 += 1
                v4[v9] += 1
                v6 = max(v6, v4[v9])
                v7 += 1
                if v7 % v5 == 0 and v7 // v5 == v6:
                    v2 = max(v2, v7)
                v8 += 1
        return v2
