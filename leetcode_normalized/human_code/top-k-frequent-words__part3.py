class C1(object):

    def topKFrequent(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = [[] for v3 in range(len(a1) + 1)]
        for v4, v5 in v1.items():
            v2[v5].append(v4)
        v6 = []
        for v7 in reversed(range(len(a1))):
            for v4 in v2[v7]:
                v6.append((-v7, v4))
            if len(v6) >= a2:
                break
        v6.sort()
        return [pair[1] for v8 in v6[:a2]]
from collections import Counter

class C2(object):

    def topKFrequent(self, a1, a2):
        """
        """
        v1 = Counter(a1)
        v2 = list(v1.keys())
        v2.sort(key=lambda w: (-v1[w], w))
        return v2[:a2]
