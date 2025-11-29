class C1(object):

    def clumsy(self, a1):
        """
        """
        if a1 <= 2:
            return a1
        if a1 <= 4:
            return a1 + 3
        if a1 % 4 == 0:
            return a1 + 1
        elif a1 % 4 <= 2:
            return a1 + 2
        return a1 - 1
