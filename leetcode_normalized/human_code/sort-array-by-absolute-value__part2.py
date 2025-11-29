class C1(object):

    def sortByAbsoluteValue(self, a1):
        """
        """
        a1.sort(key=lambda x: abs(x))
        return a1
