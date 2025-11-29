from collections import Counter

class Solution:
    def findLHS(self, nums):
        freq = Counter(nums)
        longest = 0
        for val in freq:
            nxt = val + 1
            if nxt in freq:
                longest = max(longest, freq[val] + freq[nxt])
        return longest
