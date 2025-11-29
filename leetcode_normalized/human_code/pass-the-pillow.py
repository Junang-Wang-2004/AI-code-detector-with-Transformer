class C1(object):

    def passThePillow(self, a1, a2):
        """
        """
        return a1 - abs(a1 - 1 - a2 % (2 * (a1 - 1)))
