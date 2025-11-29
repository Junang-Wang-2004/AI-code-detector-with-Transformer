class C1(object):

    def checkPalindromeFormation(self, a1, a2):
        """
        """

        def is_palindrome(a1, a2, a3):
            while a2 < a3:
                if a1[a2] != a1[a3]:
                    return False
                a2 += 1
                a3 -= 1
            return True

        def check(a1, a2):
            v1, v2 = (0, len(a2) - 1)
            while v1 < v2:
                if a1[v1] != a2[v2]:
                    return is_palindrome(a1, v1, v2) or is_palindrome(a2, v1, v2)
                v1 += 1
                v2 -= 1
            return True
        return check(a1, a2) or check(a2, a1)
