class C1(object):

    def possibleStringCount(self, a1):
        """
        """
        return len(a1) - sum((a1[i] != a1[i + 1] for v1 in range(len(a1) - 1)))
