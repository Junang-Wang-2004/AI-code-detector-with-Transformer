from collections import Counter
from heapq import heappush, heappop

class C1(object):

    def rearrangeString(self, a1, a2):
        """
        """
        if a2 <= 1:
            return a1
        v1 = Counter(a1)
        v2 = []
        for v3, v4 in v1.items():
            heappush(v2, [-v4, v3])
        v5 = []
        while v2:
            v6 = []
            for v7 in range(min(a2, len(a1) - len(v5))):
                if not v2:
                    return ''
                v8 = heappop(v2)
                v5.append(v8[1])
                v8[0] += 1
                if v8[0] < 0:
                    v6.append(v8)
            for v8 in v6:
                heappush(v2, v8)
        return ''.join(v5)
