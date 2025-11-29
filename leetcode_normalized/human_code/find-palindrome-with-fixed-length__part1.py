class C1(object):

    def kthPalindrome(self, a1, a2):
        """
        """

        def reverse(a1):
            v1 = 0
            while a1:
                v1 = v1 * 10 + a1 % 10
                a1 //= 10
            return v1

        def f(a1, a2):
            a2 = 10 ** ((a1 - 1) // 2) + (a2 - 1)
            if a2 > 10 ** ((a1 + 1) // 2) - 1:
                return -1
            return a2 * 10 ** (a1 // 2) + reverse(a2 // 10 if a1 % 2 else a2)
        return [f(a2, x) for v1 in a1]
