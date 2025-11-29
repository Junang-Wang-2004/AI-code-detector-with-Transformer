class C1(object):

    def countElements(self, a1):
        """
        """
        v1 = min(a1)
        v2 = max(a1)
        return sum((v1 < x < v2 for v3 in a1))
