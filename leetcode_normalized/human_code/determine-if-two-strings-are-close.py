import collections

class C1(object):

    def closeStrings(self, a1, a2):
        """
        """
        if len(a1) != len(a2):
            return False
        v1, v2 = (collections.Counter(a1), collections.Counter(a2))
        return set(v1.keys()) == set(v2.keys()) and collections.Counter(iter(v1.values())) == collections.Counter(iter(v2.values()))
