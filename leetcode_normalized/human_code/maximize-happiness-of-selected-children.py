class C1(object):

    def maximumHappinessSum(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        return sum((max(a1[i] - i, 0) for v1 in range(a2)))
