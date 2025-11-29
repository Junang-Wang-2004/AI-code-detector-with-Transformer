import collections

class C1(object):

    def minimumPushes(self, a1):
        """
        """
        return sum((x * (i // (9 - 2 + 1) + 1) for v1, v2 in enumerate(sorted(iter(collections.Counter(a1).values()), reverse=True))))
