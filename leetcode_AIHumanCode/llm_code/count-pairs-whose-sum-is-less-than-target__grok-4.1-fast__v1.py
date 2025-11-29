class Solution(object):
    def countPairs(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        ptr = n - 1
        for idx in range(n - 1):
            while idx < ptr and nums[idx] + nums[ptr] >= target:
                ptr -= 1
            ans += max(0, ptr - idx)
        return ans
