class C1(object):

    def countWays(self, a1):
        """
        """
        a1.sort()
        return sum(((i == 0 or a1[i - 1] < i) and (i == len(a1) or a1[i] > i) for v1 in range(len(a1) + 1)))
