# Time:  O(nlogn)
# Space: O(n)

import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        """
        LIS = []
        def insert(target):
            left = bisect.bisect_left(LIS, target)
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target
    
        for num in nums:
            insert(num)
        return len(LIS)


