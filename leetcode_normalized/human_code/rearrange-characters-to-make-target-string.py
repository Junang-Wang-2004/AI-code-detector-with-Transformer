import collections

class C1(object):

    def rearrangeCharacters(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = collections.Counter(a2)
        return min((v1[k] // v for v3, v4 in v2.items()))
