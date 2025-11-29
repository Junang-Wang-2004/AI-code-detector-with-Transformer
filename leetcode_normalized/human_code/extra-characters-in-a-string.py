import collections

class C1(object):

    def minExtraChar(self, a1, a2):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a2:
            reduce(dict.__getitem__, v3, v2).setdefault('_end')
        v4 = [float('inf')] * (len(a1) + 1)
        v4[0] = 0
        for v5 in range(len(a1)):
            v4[v5 + 1] = min(v4[v5 + 1], v4[v5] + 1)
            v6 = v2
            for v7 in range(v5, len(a1)):
                if a1[v7] not in v6:
                    break
                v6 = v6[a1[v7]]
                if '_end' in v6:
                    v4[v7 + 1] = min(v4[v7 + 1], v4[v5])
        return v4[-1]
