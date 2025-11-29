# Time:  O(n)
# Space: O(n)

import collections


# freq table, combinatorics
class Solution(object):
    def countTrapezoids(self, points):
        """
        """
        MOD = 10**9+7
        cnt = collections.defaultdict(int)
        for _, y in points:
            cnt[y] += 1
        result = total = 0
        for c in cnt.values():
            curr = (c*(c-1)//2)%MOD
            result = (result+(total*curr)%MOD)%MOD
            total = (total+curr)%MOD
        return result
