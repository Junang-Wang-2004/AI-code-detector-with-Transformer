class Solution(object):
    def subsequenceSumAfterCapping(self, nums, k):
        n = len(nums)
        output = [False] * n
        nums.sort()
        can_reach = [False] * (k + 1)
        can_reach[0] = True
        cursor = 0
        for cap_val in range(1, n + 1):
            while cursor < n and nums[cursor] < cap_val:
                value = nums[cursor]
                temp = can_reach[:]
                for prev_sum in range(k - value + 1):
                    if can_reach[prev_sum]:
                        temp[prev_sum + value] = True
                can_reach = temp
                cursor += 1
            num_remaining = n - cursor
            modulo = k % cap_val
            lower_limit = max(modulo, k - num_remaining * cap_val)
            hit = False
            test_sum = lower_limit
            while test_sum <= k:
                if can_reach[test_sum]:
                    hit = True
                    break
                test_sum += cap_val
            output[cap_val - 1] = hit
        return output
