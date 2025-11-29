# Time:  O(n)
# Space: O(1)
# array
class Solution2(object):
    def longestMonotonicSubarray(self, nums):
        """
        """
        result = cnt1 = cnt2 = 1
        for i in range(1, len(nums)):
            cnt1 = cnt1+1 if nums[i-1] < nums[i] else 1
            cnt2 = cnt2+1 if nums[i-1] > nums[i] else 1
            result = max(result, cnt1, cnt2)
        return result


