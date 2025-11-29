import collections

class C1(object):

    def canArrange(self, a1, a2):
        """
        """
        v1 = collections.Counter((i % a2 for v2 in a1))
        return (0 not in v1 or not v1[0] % 2) and all((a2 - v2 in v1 and v1[v2] == v1[a2 - v2] for v2 in range(1, a2) if v2 in v1))
