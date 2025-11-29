import collections

class C1(object):

    def commonChars(self, a1):
        """
        """
        v1 = collections.Counter(a1[0])
        for v2 in a1:
            v1 &= collections.Counter(v2)
        return list(v1.elements())
