from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        freq = Counter(nums)
        count = 0
        if k == 0:
            for occurrences in freq.values():
                if occurrences > 1:
                    count += 1
        else:
            for value in freq:
                if value + k in freq:
                    count += 1
        return count
