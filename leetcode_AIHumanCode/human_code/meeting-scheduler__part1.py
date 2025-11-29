# Time:  O(n) ~ O(nlogn)
# Space: O(n)

import heapq


class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        """
        min_heap = list([slot for slot in slots1 + slots2 if slot[1] - slot[0] >= duration])
        heapq.heapify(min_heap)  # Time: O(n)
        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)  # Time: O(logn)
            right = min_heap[0]
            if left[1]-right[0] >= duration:
                return [right[0], right[0]+duration] 
        return []   


