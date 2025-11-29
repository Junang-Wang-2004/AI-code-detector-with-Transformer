import collections

class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        return sum((v * (v + 1) // 2 for v1 in collections.Counter(a1).values()))
