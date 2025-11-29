class C1(object):

    def findFinalValue(self, a1, a2):
        """
        """
        v1 = set(a1)
        while a2 in v1:
            a2 *= 2
        return a2
