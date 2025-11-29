class C1(object):

    def findMaxK(self, a1):
        """
        """
        v1 = set(a1)
        return max([x for v2 in v1 if v2 > 0 and -v2 in v1] or [-1])
