class C1(object):

    def minimumRemoval(self, a1):
        """
        """
        a1.sort()
        return sum(a1) - max((x * (len(a1) - i) for v1, v2 in enumerate(a1)))
