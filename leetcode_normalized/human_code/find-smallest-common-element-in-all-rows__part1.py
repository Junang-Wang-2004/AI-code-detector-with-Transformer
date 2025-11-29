class C1(object):

    def smallestCommonElement(self, a1):
        """
        """
        v1 = set(a1[0])
        for v2 in range(1, len(a1)):
            v1 &= set(a1[v2])
            if not v1:
                return -1
        return min(v1)
