class C1(object):

    def maximizeGreatness(self, a1):
        """
        """
        return len(a1) - max(collections.Counter(a1).values())
