class C1(object):

    def minMoves(self, a1, a2):
        """
        """
        v1 = 0
        while a1 > 1 and a2:
            v1 += 1 + a1 % 2
            a1 //= 2
            a2 -= 1
        return v1 + (a1 - 1)
