import heapq

class C1(object):

    def smallestChair(self, a1, a2):
        """
        """
        v1 = []
        for v2, (v3, v4) in enumerate(a1):
            v1.append((v3, True, v2))
            v1.append((v4, False, v2))
        v1.sort()
        v5 = {}
        v6 = []
        for v7, v8, v2 in v1:
            if not v8:
                heapq.heappush(v6, v5.pop(v2))
                continue
            v5[v2] = heapq.heappop(v6) if v6 else len(v5)
            if v2 == a2:
                break
        return v5[a2]
