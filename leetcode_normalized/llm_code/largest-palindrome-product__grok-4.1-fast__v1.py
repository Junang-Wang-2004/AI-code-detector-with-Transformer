class C1(object):

    def largestPalindrome(self, a1):
        if a1 == 1:
            return 9
        v1 = 10 ** (a1 - 1)
        v2 = 10 ** a1 - 1
        for v3 in range(v2, v1 - 1, -1):
            v4 = int(str(v3) + str(v3)[::-1])
            v5 = min(v2, v4 // v1)
            v6 = max(v1, (v4 + v2 - 1) // v2)
            for v7 in range(v5, v6 - 1, -1):
                if v4 % v7 == 0:
                    return v4 % 1337
        return -1
