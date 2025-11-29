import heapq

class C1(object):

    def __init__(self, a1=0, a2=0):
        self.start = a1
        self.end = a2

class C2(object):

    def employeeFreeTime(self, a1):
        """
        """
        v1 = []
        v2 = [(emp[0].start, eid, 0) for v3, v4 in enumerate(a1)]
        heapq.heapify(v2)
        v5 = -1
        while v2:
            v6, v3, v7 = heapq.heappop(v2)
            if 0 <= v5 < v6:
                v1.append(C1(v5, v6))
            v5 = max(v5, a1[v3][v7].end)
            if v7 + 1 < len(a1[v3]):
                heapq.heappush(v2, (a1[v3][v7 + 1].start, v3, v7 + 1))
        return v1
