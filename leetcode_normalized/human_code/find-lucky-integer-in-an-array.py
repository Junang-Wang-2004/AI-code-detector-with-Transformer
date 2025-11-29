import collections

class C1(object):

    def findLucky(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = -1
        for v3, v4 in v1.items():
            if v3 == v4:
                v2 = max(v2, v3)
        return v2
