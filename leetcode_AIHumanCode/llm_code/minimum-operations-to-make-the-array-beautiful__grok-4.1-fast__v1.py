class Solution:
    def minOperations(self, nums):
        if not nums:
            return 0
        maxv = max(nums)
        if maxv == 1:
            return 0
        states = {nums[0]: 0}
        lim = 2 * maxv - 1
        for idx in range(1, len(nums)):
            target = nums[idx]
            next_states = {}
            for base, val in states.items():
                lo = (target + base - 1) // base
                hi = lim // base
                for mult in range(lo, hi + 1):
                    spot = mult * base
                    if spot > lim:
                        break
                    nc = val + spot - target
                    if spot not in next_states or nc < next_states[spot]:
                        next_states[spot] = nc
            states = next_states
        return min(states.values())
