class C1(object):

    def findNumbers(self, a1):
        """
        """
        return sum((len(str(n)) % 2 == 0 for v1 in a1))
