class C1(object):

    def findKOr(self, a1, a2):
        """
        """
        return sum((1 << i for v1 in range(max(a1).bit_length()) if sum((x & 1 << v1 != 0 for v2 in a1)) >= a2))
