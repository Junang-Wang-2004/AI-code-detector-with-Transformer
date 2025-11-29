class Solution(object):
    def minCost(self, nums):
        states = {nums[0]: 0}
        pos = 1
        while pos < len(nums) - 1:
            next_states = {}
            a_val, b_val = nums[pos], nums[pos + 1]
            for c_val, prev_cost in states.items():
                group = sorted([a_val, b_val, c_val])
                cost_for_min = prev_cost + group[2]
                next_states[group[0]] = min(next_states.get(group[0], float('inf')), cost_for_min)
                cost_for_max = prev_cost + group[1]
                next_states[group[2]] = min(next_states.get(group[2], float('inf')), cost_for_max)
            states = next_states
            pos += 2
        trailing = nums[-1] if len(nums) % 2 == 0 else 0
        result = min(prev_cost + max(key_val, trailing) for key_val, prev_cost in states.items())
        return result
