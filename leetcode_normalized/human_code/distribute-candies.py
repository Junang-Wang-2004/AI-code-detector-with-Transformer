class C1(object):

    def distributeCandies(self, a1):
        """
        """
        v1 = set(a1)
        return min(len(v1), len(a1) / 2)
