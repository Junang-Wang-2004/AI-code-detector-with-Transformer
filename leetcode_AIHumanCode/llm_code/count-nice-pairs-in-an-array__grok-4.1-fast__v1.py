class Solution:
    def countNicePairs(self, nums):
        MOD = 10**9 + 7
        
        def reverse_num(n):
            return int(str(n)[::-1])
        
        freq = {}
        for val in nums:
            delta = val - reverse_num(val)
            freq[delta] = freq.get(delta, 0) + 1
        
        ans = 0
        for cnt in freq.values():
            ans = (ans + cnt * (cnt - 1) // 2) % MOD
        return ans
