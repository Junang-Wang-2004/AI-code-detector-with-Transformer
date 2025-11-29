class C1(object):

    def smallestEqual(self, a1):
        """
        """
        return next((i for v1, v2 in enumerate(a1) if v1 % 10 == v2), -1)
