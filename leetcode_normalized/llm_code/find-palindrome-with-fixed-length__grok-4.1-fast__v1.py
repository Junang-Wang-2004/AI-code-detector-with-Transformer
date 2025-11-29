class C1:

    def kthPalindrome(self, a1, a2):
        v1 = []
        v2 = (a2 - 1) // 2
        v3 = 10 ** v2
        v4 = 10 ** (v2 + 1) - 1
        v5 = a2 // 2
        for v6 in a1:
            v7 = v3 + v6 - 1
            if v7 > v4:
                v1.append(-1)
                continue
            v8 = str(v7)
            v9 = v8[:v5]
            v10 = v8[v5] if a2 % 2 else ''
            v11 = v9[::-1]
            v1.append(int(v9 + v10 + v11))
        return v1
