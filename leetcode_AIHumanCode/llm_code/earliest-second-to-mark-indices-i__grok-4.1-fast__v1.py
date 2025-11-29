class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        n = len(nums)
        m = len(changeIndices)
        prefix_sum = sum(nums) + n

        def feasible(time):
            recent = [-1] * n
            for idx in range(time):
                recent[changeIndices[idx] - 1] = idx
            if -1 in recent:
                return False
            surplus = 0
            for idx in range(time):
                pile = changeIndices[idx] - 1
                if idx == recent[pile]:
                    surplus -= nums[pile]
                else:
                    surplus += 1
                if surplus < 0:
                    return False
            return True

        l, r = prefix_sum, m
        while l <= r:
            md = l + (r - l) // 2
            if feasible(md):
                r = md - 1
            else:
                l = md + 1
        return l if l <= m else -1
