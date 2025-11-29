import collections

class C1(object):

    def queryResults(self, a1, a2):
        """
        """
        v1 = [0] * len(a2)
        v2 = {}
        v3 = collections.Counter()
        for v4, (v5, v6) in enumerate(a2):
            if v5 in v2:
                v3[v2[v5]] -= 1
                if not v3[v2[v5]]:
                    del v3[v2[v5]]
            v2[v5] = v6
            v3[v2[v5]] += 1
            v1[v4] = len(v3)
        return v1
