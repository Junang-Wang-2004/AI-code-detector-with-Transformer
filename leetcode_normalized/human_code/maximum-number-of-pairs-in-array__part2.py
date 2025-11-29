import collections

class C1(object):

    def numberOfPairs(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = sum((x // 2 for v3 in v1.values()))
        return [v2, len(a1) - 2 * v2]
