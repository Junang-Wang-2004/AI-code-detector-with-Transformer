class C1(object):

    def uniqueXorTriplets(self, a1):
        """
        """
        return 1 << len(a1).bit_length() if len(a1) >= 3 else len(a1)
