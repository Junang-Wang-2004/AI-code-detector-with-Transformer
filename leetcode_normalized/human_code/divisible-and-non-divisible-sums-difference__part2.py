class C1(object):

    def differenceOfSums(self, a1, a2):
        """
        """
        return (a1 + 1) * a1 // 2 - 2 * ((a1 // a2 + 1) * (a1 // a2) // 2 * a2)
