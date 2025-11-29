class C1(object):

    def findLUSlength(self, a1, a2):
        """
        """
        if a1 == a2:
            return -1
        return max(len(a1), len(a2))
