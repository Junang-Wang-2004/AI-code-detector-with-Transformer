class C1:

    def makeAntiPalindrome(self, a1):
        v1 = len(a1)
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        if max(v2) > v1 // 2:
            return '-1'
        v4 = [0] * v1

        def pick(a1=-1):
            for v1 in range(26):
                if v2[v1] > 0 and v1 != a1:
                    return v1
            return -1
        for v5 in range(v1 // 2):
            v6 = pick()
            v4[v5] = v6
            v2[v6] -= 1
            v7 = pick(v6)
            v4[v1 - 1 - v5] = v7
            v2[v7] -= 1
        if v1 % 2:
            v4[v1 // 2] = pick()
        return ''.join((chr(ord('a') + x) for v8 in v4))
