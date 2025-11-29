import collections
import heapq

class C1(object):

    def rearrangeString(self, a1, a2):
        if a2 <= 1:
            return a1
        v1 = len(a1)
        v2 = collections.Counter(a1)
        v3 = []
        for v4, v5 in v2.items():
            heapq.heappush(v3, [-v5, v4])
        v6 = []
        while len(v6) < v1:
            v7 = []
            v8 = min(a2, v1 - len(v6))
            v9 = 0
            while v9 < v8 and v3:
                v10 = heapq.heappop(v3)
                v6.append(v10[1])
                v10[0] += 1
                v9 += 1
                if v10[0] < 0:
                    v7.append(v10)
            if v9 < v8:
                return ''
            for v11 in v7:
                heapq.heappush(v3, v11)
        return ''.join(v6)
