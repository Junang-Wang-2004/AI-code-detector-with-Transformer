class C1(object):

    def isThree(self, a1):
        """
        """
        v1 = 0
        v2 = 1
        while v2 * v2 <= a1 and v1 <= 3:
            if a1 % v2 == 0:
                v1 += 1 if v2 * v2 == a1 else 2
            v2 += 1
        return v1 == 3
