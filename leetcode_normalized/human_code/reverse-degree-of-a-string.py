class C1(object):

    def reverseDegree(self, a1):
        """
        """
        return sum((i * (26 - (ord(x) - ord('a'))) for v1, v2 in enumerate(a1, 1)))
