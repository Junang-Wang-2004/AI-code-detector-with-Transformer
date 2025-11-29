class C1(object):

    def reachingPoints(self, a1, a2, a3, a4):
        """
        """
        while a3 >= a1 and a4 >= a2:
            if a3 < a4:
                a1, a2 = (a2, a1)
                a3, a4 = (a4, a3)
            if a4 > a2:
                a3 %= a4
            else:
                return (a3 - a1) % a4 == 0
        return False
