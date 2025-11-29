class C1(object):

    def makeAntiPalindrome(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        if max(v1) > len(a1) // 2:
            return '-1'
        v3 = [i for v4, v2 in enumerate(v1) for v5 in range(v2)]
        v6 = next((v6 for v6 in range(len(a1) // 2 // 2 + 1) if v3[len(a1) // 2 + v6] != v3[len(a1) // 2 - 1]))
        if v6:
            for v4 in range(v1[v3[len(a1) // 2 - 1]] - v6):
                v3[len(a1) // 2 + v4], v3[len(a1) // 2 + v4 + v6] = (v3[len(a1) // 2 + v4 + v6], v3[len(a1) // 2 + v4])
        return ''.join([chr(ord('a') + v2) for v2 in v3])
