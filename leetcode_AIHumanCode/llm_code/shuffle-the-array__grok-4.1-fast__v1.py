class Solution(object):
    def shuffle(self, nums, n):
        MASK = (1 << 10) - 1
        SHIFT = 10
        m = len(nums)
        for i in range(n):
            nums[i] = (nums[i] << SHIFT) | nums[n + i]
        for i in range(m):
            if i % 2 == 0:
                nums[i] >>= SHIFT
            else:
                nums[i] &= MASK
        return nums
