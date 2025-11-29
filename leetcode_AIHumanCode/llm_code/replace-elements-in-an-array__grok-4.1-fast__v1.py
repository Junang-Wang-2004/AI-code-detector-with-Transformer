class Solution(object):
    def arrayChange(self, nums, operations):
        val_pos = {}
        for i, v in enumerate(nums):
            val_pos[v] = i
        for pair in operations:
            a, b = pair
            val_pos[b] = val_pos.pop(a)
        for v, i in val_pos.items():
            nums[i] = v
        return nums
