import collections

class C1(object):

    def uniqueOccurrences(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = set()
        for v3 in v1.values():
            if v3 in v2:
                return False
            v2.add(v3)
        return True
