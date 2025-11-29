class C1(object):

    def canSplitArray(self, a1, a2):
        """
        """
        return len(a1) <= 2 or any((a1[i] + a1[i + 1] >= a2 for v1 in range(len(a1) - 1)))
