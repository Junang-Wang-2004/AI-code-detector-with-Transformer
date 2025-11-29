import collections
import functools

class C1(object):

    def minimumLengthEncoding(self, a1):
        """
        """
        a1 = list(set(a1))
        v2 = lambda: collections.defaultdict(v2)
        v3 = v2()
        v4 = [functools.reduce(dict.__getitem__, word[::-1], v3) for v5 in a1]
        return sum((len(v5) + 1 for v6, v5 in enumerate(a1) if len(v4[v6]) == 0))
