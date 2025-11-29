class C1(object):

    def breakPalindrome(self, a1):
        """
        """
        for v1 in range(len(a1) // 2):
            if a1[v1] != 'a':
                return a1[:v1] + 'a' + a1[v1 + 1:]
        return a1[:-1] + 'b' if len(a1) >= 2 else ''
