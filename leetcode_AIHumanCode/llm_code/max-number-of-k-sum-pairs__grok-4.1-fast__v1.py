import collections

class Solution(object):
    def maxOperations(self, nums, k):
        freq = collections.Counter(nums)
        total = 0
        for num in freq:
            comp = k - num
            if comp < num:
                continue
            if comp == num:
                total += freq[num] // 2
            else:
                total += min(freq[num], freq[comp])
        return total
