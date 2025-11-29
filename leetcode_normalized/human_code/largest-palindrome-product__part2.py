class C1(object):

    def largestPalindrome(self, a1):
        """
        """

        def divide_ceil(a1, a2):
            return (a1 + a2 - 1) // a2
        if a1 == 1:
            return 9
        v1, v2 = (10 ** a1 - 1, 10 ** (a1 - 1))
        for v3 in reversed(range(v2, v1 ** 2 // 10 ** a1 + 1)):
            v4 = int(str(v3) + str(v3)[::-1])
            for v5 in reversed(range(divide_ceil(v2, 11) * 11, v1 + 1, 11)):
                if v4 // v5 > v1:
                    break
                if v4 % v5 == 0 and v2 <= v4 // v5:
                    return v4 % 1337
        return -1
