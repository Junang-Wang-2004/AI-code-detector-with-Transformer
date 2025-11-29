class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        res = []
        def backtrack(pos, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            for idx in range(pos, len(nums)):
                if idx > pos and nums[idx] == nums[idx - 1]:
                    continue
                if nums[idx] > remain:
                    break
                path.append(nums[idx])
                backtrack(idx + 1, path, remain - nums[idx])
                path.pop()
        backtrack(0, [], target)
        return res
