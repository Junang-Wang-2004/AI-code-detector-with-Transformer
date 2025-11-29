import collections

class C1(object):

    def mostFrequentEven(self, a1):
        """
        """
        v1 = collections.Counter((x for v2 in a1 if v2 % 2 == 0))
        return max(iter(v1.keys()), key=lambda x: (v1[v2], -v2)) if v1 else -1
