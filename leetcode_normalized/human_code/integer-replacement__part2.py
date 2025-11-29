class C1(object):

    def integerReplacement(self, a1):
        """
        """
        if a1 < 4:
            return [0, 0, 1, 2][a1]
        if a1 % 4 in (0, 2):
            return self.integerReplacement(a1 / 2) + 1
        elif a1 % 4 == 1:
            return self.integerReplacement((a1 - 1) / 4) + 3
        else:
            return self.integerReplacement((a1 + 1) / 4) + 3
