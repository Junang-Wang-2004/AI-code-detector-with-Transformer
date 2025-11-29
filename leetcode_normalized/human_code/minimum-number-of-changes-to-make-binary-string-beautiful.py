class C1(object):

    def minChanges(self, a1):
        """
        """
        return sum((a1[i] != a1[i + 1] for v1 in range(0, len(a1), 2)))
