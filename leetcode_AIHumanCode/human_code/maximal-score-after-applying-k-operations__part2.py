# Time:  O(n + klogn)
# Space: O(1)
import heapq


# heap
class Solution2(object):
    def maxKelements(self, nums, k):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        result = 0
        for i, x in enumerate(nums):
            nums[i] = -x
        heapq.heapify(nums)
        for _ in range(k):
            x = -heapq.heappop(nums)
            result += x
            heapq.heappush(nums, -ceil_divide(x, 3))
        return result
  
