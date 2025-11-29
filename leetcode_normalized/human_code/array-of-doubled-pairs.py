import collections

class C1(object):

    def canReorderDoubled(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        for v2 in sorted(v1, key=abs):
            if v1[v2] > v1[2 * v2]:
                return False
            v1[2 * v2] -= v1[v2]
        return True
