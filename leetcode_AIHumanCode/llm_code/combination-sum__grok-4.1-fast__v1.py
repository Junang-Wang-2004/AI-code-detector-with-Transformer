class Solution:
    def combinationSum(self, candidates, target):
        nums = sorted(candidates)
        ans = []
        def backtrack(idx, current, total):
            if total == 0:
                ans.append(list(current))
                return
            for i in range(idx, len(nums)):
                if nums[i] > total:
                    break
                current.append(nums[i])
                backtrack(i, current, total - nums[i])
                current.pop()
        backtrack(0, [], target)
        return ans
