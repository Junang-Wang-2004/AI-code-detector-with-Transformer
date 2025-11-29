class Solution:
    def maxNonOverlapping(self, nums, target):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        sum_to_idx = {0: 0}
        cnt = 0
        last_end = -1
        for end in range(1, n + 1):
            curr = pref[end]
            need = curr - target
            if need in sum_to_idx and sum_to_idx[need] > last_end:
                last_end = end - 1
                cnt += 1
            sum_to_idx[curr] = end
        return cnt
