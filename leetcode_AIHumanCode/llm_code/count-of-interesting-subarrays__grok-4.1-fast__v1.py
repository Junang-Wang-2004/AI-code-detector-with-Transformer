class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        freq = [0] * modulo
        freq[0] = 1
        ans = 0
        cur = 0
        for num in nums:
            cur = (cur + (1 if num % modulo == k else 0)) % modulo
            target = (cur - k) % modulo
            ans += freq[target]
            freq[cur] += 1
        return ans
