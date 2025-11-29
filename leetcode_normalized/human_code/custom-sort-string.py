import collections

class C1(object):

    def customSortString(self, a1, a2):
        """
        """
        v1, v2 = (collections.Counter(a2), set(a1))
        v3 = [c * v1[c] for v4 in a1]
        v3.extend([v4 * v1 for v4, v1 in v1.items() if v4 not in v2])
        return ''.join(v3)
