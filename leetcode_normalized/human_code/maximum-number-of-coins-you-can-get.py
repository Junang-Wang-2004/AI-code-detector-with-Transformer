import itertools

class C1(object):

    def maxCoins(self, a1):
        """
        """
        a1.sort()
        return sum(itertools.islice(a1, len(a1) // 3, len(a1), 2))
