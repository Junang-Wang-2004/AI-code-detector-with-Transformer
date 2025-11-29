class Solution:
    def transformArray(self, nums):
        while True:
            next_state = nums[:]
            has_change = False
            for idx in range(1, len(nums) - 1):
                prev, curr, nxt = nums[idx - 1], nums[idx], nums[idx + 1]
                if prev > curr and curr < nxt:
                    next_state[idx] += 1
                    has_change = True
                elif prev < curr and curr > nxt:
                    next_state[idx] -= 1
                    has_change = True
            nums = next_state
            if not has_change:
                break
        return nums
