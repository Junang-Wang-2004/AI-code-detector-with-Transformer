class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        answer = 0
        for end in range(n):
            left, right = 0, end + 1
            while left < right:
                m = (left + right) // 2
                sub_sum = pref[end + 1] - pref[m]
                sub_len = end - m + 1
                if sub_sum * sub_len < k:
                    right = m
                else:
                    left = m + 1
            start_pos = left
            answer += end - start_pos + 1
        return answer
