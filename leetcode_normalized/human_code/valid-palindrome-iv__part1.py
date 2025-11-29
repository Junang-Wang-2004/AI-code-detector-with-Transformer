class C1(object):

    def makePalindrome(self, a1):
        """
        """
        return sum((a1[i] != a1[~i] for v1 in range(len(a1) // 2))) <= 2
