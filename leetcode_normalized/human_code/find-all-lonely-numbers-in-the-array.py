class C1(object):

    def findLonely(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return [x for v2 in a1 if v1[v2] == 1 and v2 - 1 not in v1 and (v2 + 1 not in v1)]
