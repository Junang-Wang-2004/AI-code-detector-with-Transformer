class C1(object):

    def isConsecutive(self, a1):
        """
        """
        return max(a1) - min(a1) + 1 == len(a1) == len(set(a1))
