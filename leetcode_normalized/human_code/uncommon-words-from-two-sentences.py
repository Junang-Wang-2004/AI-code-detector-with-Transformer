import collections

class C1(object):

    def uncommonFromSentences(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1.split())
        v1 += collections.Counter(a2.split())
        return [word for v2 in v1 if v1[v2] == 1]
