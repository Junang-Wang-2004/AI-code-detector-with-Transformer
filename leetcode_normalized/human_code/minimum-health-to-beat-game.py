class C1(object):

    def minimumHealth(self, a1, a2):
        """
        """
        return sum(a1) - min(max(a1), a2) + 1
