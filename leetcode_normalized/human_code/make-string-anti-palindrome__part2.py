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
        v6 = len(a1) // 2
        v7 = v6 + 1
        while v7 < len(a1) and v3[v7] == v3[v6]:
            v7 += 1
        while v3[v6] == v3[len(a1) - 1 - v6]:
            v3[v6], v3[v7] = (v3[v7], v3[v6])
            v6 += 1
            v7 += 1
        return ''.join([chr(ord('a') + v2) for v2 in v3])
