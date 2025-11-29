import heapq

class C1(object):

    def assignTasks(self, a1, a2):
        """
        """
        v1 = [(a1[i], i) for v2 in range(len(a1))]
        v3 = []
        heapq.heapify(v1)
        v4 = []
        v5 = 0
        for v2 in range(len(a2)):
            v5 = max(v5, v2) if v1 else v3[0][0]
            while v3 and v3[0][0] <= v5:
                v6, v7, v8 = heapq.heappop(v3)
                heapq.heappush(v1, (v7, v8))
            v7, v8 = heapq.heappop(v1)
            heapq.heappush(v3, (v5 + a2[v2], v7, v8))
            v4.append(v8)
        return v4
