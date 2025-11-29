class C1(object):

    def makePalindrome(self, a1):
        """
        """
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        while v2 < v3:
            if a1[v2] != a1[v3]:
                v1 += 1
                if v1 > 2:
                    return False
            v2 += 1
            v3 -= 1
        return True
