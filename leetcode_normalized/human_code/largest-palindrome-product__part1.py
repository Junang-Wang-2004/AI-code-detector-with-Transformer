class C1(object):

    def largestPalindrome(self, a1):
        """
        """
        if a1 == 1:
            return 9
        v1 = 10 ** a1 - 1
        for v2 in range(2, v1 + 1):
            v3 = 10 ** a1 - v2
            v4 = int(str(v3)[::-1])
            v5 = v2 ** 2 - v4 * 4
            if v5 < 0:
                continue
            if v5 ** 0.5 == int(v5 ** 0.5) and v2 % 2 == int(v5 ** 0.5) % 2:
                return (v3 * 10 ** a1 + v4) % 1337
        return -1
