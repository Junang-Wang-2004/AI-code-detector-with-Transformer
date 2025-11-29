class C1(object):

    def replaceElements(self, a1):
        """
        """
        v1 = -1
        for v2 in reversed(range(len(a1))):
            a1[v2], v1 = (v1, max(v1, a1[v2]))
        return a1
