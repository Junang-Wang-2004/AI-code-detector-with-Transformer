import collections

class C1(object):

    def isPossibleDivide(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        for v2 in sorted(v1.keys()):
            v3 = v1[v2]
            if not v3:
                continue
            for v4 in range(v2, v2 + a2):
                if v1[v4] < v3:
                    return False
                v1[v4] -= v3
        return True
