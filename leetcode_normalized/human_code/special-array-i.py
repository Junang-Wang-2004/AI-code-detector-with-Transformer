class C1(object):

    def isArraySpecial(self, a1):
        """
        """
        return all((a1[i] & 1 != a1[i + 1] & 1 for v1 in range(len(a1) - 1)))
