class Solution:
    def minPatches(self, nums, n):
        patches = 0
        cover = 0
        ptr = 0
        while cover < n:
            if ptr < len(nums) and nums[ptr] <= cover + 1:
                cover += nums[ptr]
                ptr += 1
            else:
                next_val = cover + 1
                cover += next_val
                patches += 1
        return patches
