class Solution:
    def findSubsequences(self, nums):
        outcomes = []
        def explore(from_idx, current):
            if len(current) >= 2:
                outcomes.append(current)
            checked = set()
            for k in range(from_idx, len(nums)):
                if not current or nums[k] >= current[-1]:
                    if nums[k] not in checked:
                        checked.add(nums[k])
                        explore(k + 1, current + [nums[k]])
        explore(0, [])
        return outcomes
