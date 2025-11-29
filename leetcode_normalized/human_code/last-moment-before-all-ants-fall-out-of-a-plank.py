class C1(object):

    def getLastMoment(self, a1, a2, a3):
        """
        """
        return max(max(a2 or [0]), a1 - min(a3 or [a1]))
