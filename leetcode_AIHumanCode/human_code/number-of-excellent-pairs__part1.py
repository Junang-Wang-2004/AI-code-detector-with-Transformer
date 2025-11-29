# Time:  O(n + (logn)^2) = O(n)
# Space: O(n + logn) = O(n)

import collections


# bit manipulation, freq table, combinatorics
class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        cnt = collections.Counter(popcount(x) for x in set(nums))
        return sum(cnt[i]*cnt[j] for i in cnt.keys() for j in cnt.keys() if i+j >= k)


