class C1:

    def smallestPalindrome(self, a1: str) -> str:
        v1 = len(a1)
        v2 = v1 // 2
        v3 = [0] * 26
        for v4 in a1[:v2]:
            v3[ord(v4) - ord('a')] += 1
        v5 = ''
        v6 = ord('a')
        for v7 in range(26):
            v5 += chr(v6 + v7) * v3[v7]
        v8 = v5[::-1]
        if v1 % 2:
            return v5 + a1[v2] + v8
        return v5 + v8
