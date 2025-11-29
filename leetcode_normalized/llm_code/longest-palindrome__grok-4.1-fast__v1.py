class C1:

    def longestPalindrome(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = sum((v % 2 for v4 in v1.values()))
        return len(a1) - max(0, v3 - 1)
