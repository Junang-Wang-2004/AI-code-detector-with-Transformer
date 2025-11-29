import collections

class C1(object):

    def countWords(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        for v2 in a2:
            if v1[v2] < 2:
                v1[v2] -= 1
        return sum((v == 0 for v3 in v1.values()))
