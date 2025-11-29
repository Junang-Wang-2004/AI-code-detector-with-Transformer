import collections

class C1(object):

    def areOccurrencesEqual(self, a1):
        """
        """
        return len(set(collections.Counter(a1).values())) == 1
