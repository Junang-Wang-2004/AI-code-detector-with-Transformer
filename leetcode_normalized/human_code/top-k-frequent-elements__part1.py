import collections

class C1(object):

    def topKFrequent(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = [[] for v3 in range(len(a1) + 1)]
        for v4, v5 in v1.items():
            v2[v5].append(v4)
        v6 = []
        for v4 in reversed(range(len(v2))):
            for v7 in range(len(v2[v4])):
                v6.append(v2[v4][v7])
                if len(v6) == a2:
                    return v6
        return v6
