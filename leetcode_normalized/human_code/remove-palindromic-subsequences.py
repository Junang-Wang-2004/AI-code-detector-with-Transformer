class C1(object):

    def removePalindromeSub(self, a1):
        """
        """

        def is_palindrome(a1):
            for v1 in range(len(a1) // 2):
                if a1[v1] != a1[-1 - v1]:
                    return False
            return True
        return 2 - is_palindrome(a1) - (a1 == '')
