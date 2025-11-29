class C1(object):

    def findMissingElements(self, a1):
        """
        """
        v1 = set(a1)
        return [x for v2 in range(min(a1) + 1, max(a1)) if v2 not in v1]
