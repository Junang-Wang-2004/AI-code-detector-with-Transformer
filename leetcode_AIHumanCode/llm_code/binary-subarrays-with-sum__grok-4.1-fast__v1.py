class Solution(object):
    def numSubarraysWithSum(self, A, S):
        freq = {0: 1}
        prefix = 0
        total = 0
        for val in A:
            prefix += val
            total += freq.get(prefix - S, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        return total
