class C1(object):

    def longestPalindrome(self, a1):
        """
        """

        def expand(a1, a2, a3):
            while a2 >= 0 and a3 < len(a1) and (a1[a2] == a1[a3]):
                a2 -= 1
                a3 += 1
            return a3 - a2 + 1 - 2
        v1, v2 = (-1, -2)
        for v3 in range(len(a1)):
            v4 = max(expand(a1, v3, v3), expand(a1, v3, v3 + 1))
            if v4 > v2 - v1 + 1:
                v2 = v3 + v4 // 2
                v1 = v2 - v4 + 1
        return a1[v1:v2 + 1] if v1 >= 0 else ''
