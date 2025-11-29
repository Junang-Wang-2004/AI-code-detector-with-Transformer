class C1:

    def longestCommonPrefix(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v3 = v1
            for v4 in str(v2):
                if v4 not in v3:
                    v3[v4] = {}
                v3 = v3[v4]
        v5 = 0
        for v2 in a2:
            v3 = v1
            v6 = 0
            for v4 in str(v2):
                if v4 not in v3:
                    break
                v3 = v3[v4]
                v6 += 1
            v5 = max(v5, v6)
        return v5
