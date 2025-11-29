import collections

class C1(object):

    def minimumKeypresses(self, a1):
        """
        """
        return sum((cnt * (i // 9 + 1) for v1, v2 in enumerate(sorted(iter(collections.Counter(a1).values()), reverse=True))))
