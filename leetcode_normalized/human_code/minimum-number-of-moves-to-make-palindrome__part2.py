class C1(object):

    def minMovesToMakePalindrome(self, a1):
        """
        """
        a1 = list(a1)
        v2 = 0
        while a1:
            v3 = a1.index(a1[-1])
            if v3 == len(a1) - 1:
                v2 += v3 // 2
            else:
                v2 += v3
                a1.pop(v3)
            a1.pop()
        return v2
