import itertools

class C1(object):

    def minMovesToSeat(self, a1, a2):
        """
        """
        a1.sort()
        a2.sort()
        return sum((abs(a - b) for v1, v2 in zip(a1, a2)))
