class C1(object):

    def kthPalindrome(self, a1, a2):
        """
        """

        def f(a1, a2):
            if 10 ** ((a1 - 1) // 2) + (a2 - 1) > 10 ** ((a1 + 1) // 2) - 1:
                return -1
            v1 = str(10 ** ((a1 - 1) // 2) + (a2 - 1))
            return int(v1 + v1[::-1][a1 % 2:])
        return [f(a2, x) for v1 in a1]
