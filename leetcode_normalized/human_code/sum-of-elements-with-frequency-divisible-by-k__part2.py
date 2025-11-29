import collections

class C1(object):

    def sumDivisibleByK(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        return sum((v2 for v2 in a1 if v1[v2] % a2 == 0))
