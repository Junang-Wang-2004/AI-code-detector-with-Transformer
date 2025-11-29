import heapq

class C1(object):

    def longestDiverseString(self, a1, a2, a3):
        """
        """
        v1 = []
        if a1:
            heapq.heappush(v1, (-a1, 'a'))
        if a2:
            heapq.heappush(v1, (-a2, 'b'))
        if a3:
            heapq.heappush(v1, (-a3, 'c'))
        v2 = []
        while v1:
            v3, v4 = heapq.heappop(v1)
            if len(v2) >= 2 and v2[-1] == v2[-2] == v4:
                if not v1:
                    return ''.join(v2)
                v5, v6 = heapq.heappop(v1)
                v2.append(v6)
                v5 += 1
                if v5:
                    heapq.heappush(v1, (v5, v6))
                heapq.heappush(v1, (v3, v4))
                continue
            v2.append(v4)
            v3 += 1
            if v3 != 0:
                heapq.heappush(v1, (v3, v4))
        return ''.join(v2)
