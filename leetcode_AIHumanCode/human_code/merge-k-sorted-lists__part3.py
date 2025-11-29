# Time:  O(nlogk)
# Space: O(k)
# Heap solution.
import heapq
class Solution3(object):
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.__next__
            if smallest.__next__:
                heapq.heappush(heap, (smallest.next.val, smallest.__next__))

        return dummy.__next__


