class C1(object):

    def waysToBuyPensPencils(self, a1, a2, a3):
        """
        """
        if a2 < a3:
            a2, a3 = (a3, a2)
        return sum(((a1 - i * a2) // a3 + 1 for v3 in range(a1 // a2 + 1)))
