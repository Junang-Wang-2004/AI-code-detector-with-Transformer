class C1(object):

    def firstPalindrome(self, a1):
        """
        """

        def is_palindrome(a1):
            v1, v2 = (0, len(a1) - 1)
            while v1 < v2:
                if a1[v1] != a1[v2]:
                    return False
                v1 += 1
                v2 -= 1
            return True
        for v1 in a1:
            if is_palindrome(v1):
                return v1
        return ''
