class Solution:
    def minUnlockedIndices(self, nums, locked):
        res = 0
        highest = 0
        pending = 0
        for val, is_locked in zip(nums, locked):
            if val > highest:
                highest = val
                pending = 0
            elif val < highest:
                if highest != val + 1:
                    return -1
                res += pending
                pending = 0
            pending += is_locked
        return res
