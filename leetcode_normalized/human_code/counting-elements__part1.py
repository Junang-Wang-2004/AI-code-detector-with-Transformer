class C1(object):

    def countElements(self, a1):
        """
        """
        v1 = set(a1)
        return sum((1 for v2 in a1 if v2 + 1 in v1))
