import collections

class C1(object):

    def canConstruct(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = sum((v % 2 for v3 in v1.values()))
        return v2 <= a2 <= len(a1)
