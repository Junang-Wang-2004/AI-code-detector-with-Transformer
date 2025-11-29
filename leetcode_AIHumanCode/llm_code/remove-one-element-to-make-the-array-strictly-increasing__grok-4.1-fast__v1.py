class Solution(object):
    def canBeIncreasing(self, nums):
        n = len(nums)
        pos = -1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                if pos != -1:
                    return False
                pos = i
        if pos == -1:
            return True
        skip_prev = pos <= 1 or nums[pos] > nums[pos - 2]
        skip_curr = pos >= n - 1 or nums[pos + 1] > nums[pos - 1]
        return skip_prev or skip_curr
