import collections

class C1(object):

    def shortestCompletingWord(self, a1, a2):
        """
        """

        def contains(a1, a2):
            v1 = collections.Counter(a2.lower())
            v1.subtract(a1)
            return all([x >= 0 for v2 in list(v1.values())])
        v1 = None
        v2 = collections.Counter((c.lower() for v3 in a1 if v3.isalpha()))
        for v4 in a2:
            if (v1 is None or len(v4) < len(v1)) and contains(v2, v4):
                v1 = v4
        return v1
