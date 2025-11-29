import collections
import bisect

class C1(object):

    def __init__(self, a1):
        self.pos = collections.defaultdict(list)
        for v1, v2 in enumerate(a1):
            self.pos[v2].append(v1)

    def shortest(self, a1, a2):
        v1 = self.pos[a1]
        v2 = self.pos[a2]
        if len(v1) > len(v2):
            v1, v2 = (v2, v1)
        v3 = float('inf')
        for v4 in v1:
            v5 = bisect.bisect_left(v2, v4)
            if v5 < len(v2):
                v3 = min(v3, v2[v5] - v4)
            if v5 > 0:
                v3 = min(v3, v4 - v2[v5 - 1])
        return v3
