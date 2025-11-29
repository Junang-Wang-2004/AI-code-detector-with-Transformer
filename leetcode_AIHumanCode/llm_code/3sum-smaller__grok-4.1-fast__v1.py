class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        size = len(nums)
        ans = 0
        for lo in range(size - 2):
            hi1 = lo + 1
            hi2 = size - 1
            while hi1 < hi2:
                total = nums[lo] + nums[hi1] + nums[hi2]
                if total < target:
                    ans += hi2 - hi1
                    hi1 += 1
                else:
                    hi2 -= 1
        return ans
