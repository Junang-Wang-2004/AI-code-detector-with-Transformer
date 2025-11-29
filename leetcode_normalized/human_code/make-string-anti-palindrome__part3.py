class C1(object):

    def makeAntiPalindrome(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        if max(v1) > len(a1) // 2:
            return '-1'
        v3 = [-1] * len(a1)
        for v4 in range(len(a1) // 2):
            v5 = next((v5 for v5 in range(len(v1)) if v1[v5]))
            v1[v5] -= 1
            v3[v4] = v5
        for v4 in range(len(a1) // 2, len(a1)):
            v5 = next((v5 for v5 in range(len(v1)) if v1[v5] and v3[len(a1) - 1 - v4] != v5))
            v1[v5] -= 1
            v3[v4] = v5
        return ''.join([chr(ord('a') + v2) for v2 in v3])
