from functools import reduce

class C1(object):

    def findTheWinner(self, a1, a2):
        """
        """
        return reduce(lambda idx, n: (idx + a2) % (a1 + 1), range(1, a1), 0) + 1
