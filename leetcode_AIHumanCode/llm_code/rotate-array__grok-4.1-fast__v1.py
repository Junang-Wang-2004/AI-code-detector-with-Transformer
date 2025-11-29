class Solution:
    def rotate(self, nums, k):
        total = len(nums)
        shift = k % total
        for i in range(total // 2):
            nums[i], nums[total - 1 - i] = nums[total - 1 - i], nums[i]
        for i in range(shift // 2):
            nums[i], nums[shift - 1 - i] = nums[shift - 1 - i], nums[i]
        remain = total - shift
        for i in range(remain // 2):
            nums[shift + i], nums[total - 1 - i] = nums[total - 1 - i], nums[shift + i]
