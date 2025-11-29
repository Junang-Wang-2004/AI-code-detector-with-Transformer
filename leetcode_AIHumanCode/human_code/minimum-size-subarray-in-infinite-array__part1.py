# Time:  O(n)
# Space: O(1)

# two pointers, sliding window
class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        """
        INF = float("inf")
        q, target = divmod(target, sum(nums))
        if not target:
            return q*len(nums)
        result = INF
        curr = left = 0
        for right in range((len(nums)-1)+(len(nums)-1)):
            curr += nums[right%len(nums)]
            while curr > target:
                curr -= nums[left%len(nums)]
                left += 1
            if curr == target:
                result = min(result, right-left+1)
        return result+q*len(nums) if result != INF else -1


