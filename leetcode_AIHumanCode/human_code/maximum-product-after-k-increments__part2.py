# Time:  O(n + k)
# Space: O(n)
import collections
from functools import reduce


# freq table
class Solution2(object):
    def maximumProduct(self, nums, k):
        """
        """
        MOD = 10**9+7
        cnt = collections.Counter(nums)
        min_num = min(cnt.keys())
        while k:
            c = min(cnt[min_num], k)
            cnt[min_num] -= c
            cnt[min_num+1] += c 
            if not cnt[min_num]:
                del cnt[min_num]
                min_num += 1
            k -= c
        return reduce(lambda total, x: total*pow(x[0], x[1], MOD)%MOD, iter(cnt.items()), 1)


