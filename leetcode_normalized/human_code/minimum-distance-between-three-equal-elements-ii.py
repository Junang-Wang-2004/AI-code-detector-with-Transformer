import collections

class C1(object):

    def minimumDistance(self, a1):
        """
        """
        v1 = float('inf')
        v2 = v1
        v3 = collections.defaultdict(list)
        for v4, v5 in enumerate(a1):
            v3[v5].append(v4)
            if len(v3[v5]) < 3:
                continue
            v2 = min(v2, 2 * (v4 - v3[v5][-3]))
        return v2 if v2 != v1 else -1
