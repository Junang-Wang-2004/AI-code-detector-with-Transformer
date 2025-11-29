class C1(object):

    def validPalindrome(self, a1):
        """
        """

        def validPalindrome(a1, a2, a3):
            while a2 < a3:
                if a1[a2] != a1[a3]:
                    return False
                a2, a3 = (a2 + 1, a3 - 1)
            return True
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            if a1[v1] != a1[v2]:
                return validPalindrome(a1, v1, v2 - 1) or validPalindrome(a1, v1 + 1, v2)
            v1, v2 = (v1 + 1, v2 - 1)
        return True
