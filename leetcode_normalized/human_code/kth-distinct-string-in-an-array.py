import collections

class C1(object):

    def kthDistinct(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        a1 = [x for v3 in a1 if v1[v3] == 1]
        return a1[a2 - 1] if a2 - 1 < len(a1) else ''
