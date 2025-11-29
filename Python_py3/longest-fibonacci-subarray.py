# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def longestSubarray(self, nums):
        """
        """
        result = cnt = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[i-1]+nums[i-2]:
                cnt = 2
                continue
            cnt += 1
            result = max(result, cnt)
        return result
