class C1(object):

    def haveConflict(self, a1, a2):
        """
        """
        return max(a1[0], a2[0]) <= min(a1[1], a2[1])
