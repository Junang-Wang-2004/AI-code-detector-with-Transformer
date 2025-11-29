class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        import heapq
        if not lists:
            return None
        pq = []
        count = 0
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, count, head))
                count += 1
        if not pq:
            return None
        prev = ListNode()
        walker = prev
        while pq:
            _, _, node = heapq.heappop(pq)
            walker.next = node
            walker = walker.next
            if node.next:
                count += 1
                heapq.heappush(pq, (node.next.val, count, node.next))
        return prev.next
