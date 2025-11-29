from functools import reduce

class C1(object):

    def wordCount(self, a1, a2):
        """
        """

        def bitmask(a1):
            return reduce(lambda x, y: x | y, (1 << ord(c) - ord('a') for v1, v2 in enumerate(a1)))
        v1 = set((bitmask(w) for v2 in a1))
        v3 = 0
        for v2 in a2:
            v4 = bitmask(v2)
            v3 += any((v4 ^ 1 << ord(c) - ord('a') in v1 for v5 in v2))
        return v3
