import collections

class C1(object):

    def minimumRounds(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return sum(((x + 2) // 3 for v2 in v1.values())) if 1 not in iter(v1.values()) else -1
