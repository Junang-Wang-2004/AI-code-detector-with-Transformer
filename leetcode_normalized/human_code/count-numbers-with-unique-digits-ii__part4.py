from functools import reduce

class C1(object):

    def numberCount(self, a1, a2):
        """
        """
        return sum((len(set(str(x))) == len(str(x)) for v1 in range(a1, a2 + 1)))
