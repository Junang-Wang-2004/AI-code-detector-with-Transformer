class C1(object):

    def prefixCount(self, a1, a2):
        """
        """
        return sum((x.startswith(a2) for v1 in a1))
