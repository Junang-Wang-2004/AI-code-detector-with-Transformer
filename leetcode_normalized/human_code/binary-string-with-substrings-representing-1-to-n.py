class C1(object):

    def queryString(self, a1, a2):
        """
        """
        return all((bin(i)[2:] in a1 for v1 in reversed(range(a2 // 2, a2 + 1))))
