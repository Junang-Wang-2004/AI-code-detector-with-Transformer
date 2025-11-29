class C1(object):

    def isConsecutive(self, a1):
        """
        """
        a1.sort()
        return all((a1[i] + 1 == a1[i + 1] for v1 in range(len(a1) - 1)))
