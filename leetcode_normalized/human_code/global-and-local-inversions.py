class C1(object):

    def isIdealPermutation(self, a1):
        """
        """
        return all((abs(v - i) <= 1 for v1, v2 in enumerate(a1)))
