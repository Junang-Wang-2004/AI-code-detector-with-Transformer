class Solution(object):
    def maxProduct(self, nums, k, limit):
        total_sum = sum(nums)
        if abs(k) > total_sum:
            return -1
        states = {}
        for num in nums:
            next_states = states.copy()
            if num <= limit:
                key = (1, num)
                next_states[key] = max(next_states.get(key, 0), num)
            for prev_key, prev_prod in states.items():
                parity, current_sum = prev_key
                increment = num if parity == 0 else -num
                new_sum = current_sum + increment
                new_parity = 1 - parity
                candidate_prod = prev_prod * num
                if candidate_prod <= limit:
                    new_key = (new_parity, new_sum)
                    next_states[new_key] = max(next_states.get(new_key, 0), candidate_prod)
            states = next_states
        maximum = -1
        for key, prod in states.items():
            parity, current_sum = key
            if current_sum == k:
                maximum = max(maximum, prod)
        return maximum
