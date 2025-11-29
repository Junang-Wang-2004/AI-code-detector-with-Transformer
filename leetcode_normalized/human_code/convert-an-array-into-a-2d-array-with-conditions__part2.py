import collections

class C1(object):

    def findMatrix(self, a1):
        """
        """
        v1 = []
        v2 = collections.Counter(a1)
        while v2:
            v1.append(list(v2.keys()))
            v2 = {k: v - 1 for v3, v4 in v2.items() if v4 - 1}
        return v1
