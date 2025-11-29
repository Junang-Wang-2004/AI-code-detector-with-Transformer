import collections

class C1(object):

    def findMissingAndRepeatedValues(self, a1):
        """
        """
        v1 = collections.Counter((x for v2 in a1 for v3 in v2))
        return [next((k for v4, v5 in v1.items() if v5 == 2)), next((v3 for v3 in range(1, len(a1) ** 2 + 1) if v3 not in v1))]
