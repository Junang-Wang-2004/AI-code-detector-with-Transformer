import heapq

class C1(object):

    def mergeKLists(self, a1):
        v1 = ListNode(0)
        v2 = v1
        v3 = []
        for v4 in a1:
            if v4:
                heapq.heappush(v3, (v4.val, v4))
        while v3:
            v5 = heapq.heappop(v3)[1]
            v2.next = v5
            v2 = v2.__next__
            if v5.__next__:
                heapq.heappush(v3, (v5.next.val, v5.__next__))
        return v1.__next__
