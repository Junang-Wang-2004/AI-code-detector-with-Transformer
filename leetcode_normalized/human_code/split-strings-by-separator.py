class C1(object):

    def splitWordsBySeparator(self, a1, a2):
        """
        """
        return [w for v1 in a1 for v2 in v1.split(a2) if v2]
