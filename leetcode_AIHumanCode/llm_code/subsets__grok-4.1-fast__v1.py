class Solution:
    def subsets(self, nums):
        nums.sort()
        ans = []
        def backtrack(start, current):
            ans.append(list(current))
            for pos in range(start, len(nums)):
                current.append(nums[pos])
                backtrack(pos + 1, current)
                current.pop()
        backtrack(0, [])
        return ans
