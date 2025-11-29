class C1:

    def numDecodings(self, a1):
        v1 = 1000000007
        v2 = len(a1)
        if a1[0] == '0':
            return 0
        v3 = 9 if a1[0] == '*' else 1
        v4 = 1
        for v5 in range(1, v2):
            v6 = a1[v5]
            v7 = a1[v5 - 1]
            v8 = 9 if v6 == '*' else 1 if v6 != '0' else 0
            v9 = 0
            if v7 == '1':
                v9 = 9 if v6 == '*' else 1
            elif v7 == '2':
                v9 = 6 if v6 == '*' else 1 if v6 <= '6' else 0
            elif v7 == '*':
                v9 = 15 if v6 == '*' else 2 if v6 <= '6' else 1
            v10 = (v8 * v3 + v9 * v4) % v1
            v4 = v3
            v3 = v10
        return v3
