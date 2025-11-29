# Time:  O(nlogn)
# Space: O(n)

import heapq


# greedy, heap
class Solution(object):
    def convertArray(self, nums):
        """
        """
        def f(nums):
            result = 0
            max_heap = []
            for x in nums:
                if max_heap and x < -max_heap[0]:
                    result += -heapq.heappop(max_heap)-x
                    heapq.heappush(max_heap, -x)
                heapq.heappush(max_heap, -x)
            return result
        
        return min(f(nums), f((x for x in reversed(nums))))


