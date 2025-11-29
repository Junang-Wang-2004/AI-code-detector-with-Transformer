# Time:  O(n * 2^n)
# Space: O(1)

# bitmasks
class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        """
        total = 1
        for x in nums:
            total *= x
            if total > target**2:
                return False
        if total != target**2:
            return False
        for mask in range(1, 1<<len(nums)-1):
            curr = 1
            for i in range(len(nums)):
                if not mask&(1<<i):
                    continue
                curr *= nums[i]
                if curr > target:
                    break
            if curr == target:
                return True
        return False
