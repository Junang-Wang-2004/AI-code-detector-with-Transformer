class C1:

    def uniqueLetterString(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [-1] * 26
        v4 = [-1] * 26
        v5 = 0
        for v6 in range(v2):
            v7 = ord(a1[v6]) - ord('A')
            v8 = v3[v7]
            v9 = v4[v7]
            v5 = (v5 + (v6 - v8) * (v8 - v9)) % v1
            v4[v7] = v8
            v3[v7] = v6
        for v10 in range(26):
            v8 = v3[v10]
            v9 = v4[v10]
            v5 = (v5 + (v2 - v8) * (v8 - v9)) % v1
        return v5
