class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def mergeKLists(self, a1):
        import heapq
        if not a1:
            return None
        v1 = []
        v2 = 0
        for v3 in a1:
            if v3:
                heapq.heappush(v1, (v3.val, v2, v3))
                v2 += 1
        if not v1:
            return None
        v4 = C1()
        v5 = v4
        while v1:
            v6, v6, v7 = heapq.heappop(v1)
            v5.next = v7
            v5 = v5.next
            if v7.next:
                v2 += 1
                heapq.heappush(v1, (v7.next.val, v2, v7.next))
        return v4.next
