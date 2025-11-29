class Solution:
    def permute(self, nums):
        output = []
        def backtrack(pos):
            if pos == len(nums):
                output.append(nums[:])
                return
            for j in range(pos, len(nums)):
                nums[pos], nums[j] = nums[j], nums[pos]
                backtrack(pos + 1)
                nums[pos], nums[j] = nums[j], nums[pos]
        backtrack(0)
        return output
