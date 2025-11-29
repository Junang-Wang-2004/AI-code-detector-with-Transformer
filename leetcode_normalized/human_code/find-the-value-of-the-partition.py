class C1(object):

    def findValueOfPartition(self, a1):
        """
        """
        a1.sort()
        return min((a1[i + 1] - a1[i] for v1 in range(len(a1) - 1)))
