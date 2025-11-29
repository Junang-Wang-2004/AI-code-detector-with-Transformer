import itertools

class C1(object):

    def maxGoodNumber(self, a1):
        """
        """
        return max((int(''.join(x), 2) for v1 in itertools.permutations([bin(v1)[2:] for v1 in a1])))
