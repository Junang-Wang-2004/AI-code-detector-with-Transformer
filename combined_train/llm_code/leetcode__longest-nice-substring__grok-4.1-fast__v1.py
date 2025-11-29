class C1:

    def longestNiceSubstring(self, a1):
        v1 = len(a1)
        v2 = ''
        v3 = 0
        for v4 in range(v1):
            v5 = 0
            v6 = 0
            for v7 in range(v4, v1):
                v8 = a1[v7].lower()
                v9 = ord(v8) - ord('a')
                v10 = 1 << v9
                if a1[v7].islower():
                    v5 |= v10
                else:
                    v6 |= v10
                v11 = v7 - v4 + 1
                if v5 == v6 and v11 > v3:
                    v3 = v11
                    v2 = a1[v4:v7 + 1]
        return v2
