from functools import reduce

class C1(object):

    def checkTwoChessboards(self, a1, a2):
        """
        """

        def parity(a1):
            return reduce(lambda accu, x: (accu + x) % 2, (ord(x) for v1 in a1), 0)
        return parity(a1) == parity(a2)
