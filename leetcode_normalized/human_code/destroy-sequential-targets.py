import collections

class C1(object):

    def destroyTargets(self, a1, a2):
        """
        """
        v1 = collections.Counter((x % a2 for v2 in a1))
        v3 = max(v1.values())
        return min((v2 for v2 in a1 if v1[v2 % a2] == v3))
