import collections
import heapq

class C1(object):

    def reorganizeString(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        if any((v > (len(a1) + 1) / 2 for v2, v3 in v1.items())):
            return ''
        v4 = []
        v5 = []
        for v2, v3 in v1.items():
            heapq.heappush(v5, (-v3, v2))
        while len(v5) > 1:
            v6, v7 = heapq.heappop(v5)
            v8, v9 = heapq.heappop(v5)
            if not v4 or v7 != v4[-1]:
                v4.extend([v7, v9])
                if v6 + 1:
                    heapq.heappush(v5, (v6 + 1, v7))
                if v8 + 1:
                    heapq.heappush(v5, (v8 + 1, v9))
        return ''.join(v4) + (v5[0][1] if v5 else '')
