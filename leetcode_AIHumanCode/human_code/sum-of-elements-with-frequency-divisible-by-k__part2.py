# Time:  O(n)
# Space: O(n)
import collections


# freq table
class Solution2(object):
    def sumDivisibleByK(self, nums, k):
        """
        """
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        return sum(x for x in nums if cnt[x]%k == 0)
