class Solution:
    def subarraysDivByK(self, nums, k):
        freq = {0: 1}
        cur_mod = 0
        total = 0
        for num in nums:
            cur_mod = (cur_mod + num) % k
            total += freq.get(cur_mod, 0)
            freq[cur_mod] = freq.get(cur_mod, 0) + 1
        return total
