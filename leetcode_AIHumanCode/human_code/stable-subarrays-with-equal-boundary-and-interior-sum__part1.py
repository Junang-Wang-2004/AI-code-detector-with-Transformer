# Time:  O(n)
# Space: O(n)

import collections


# freq table, prefix sum
class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        """
        L = 3
        cnt = collections.defaultdict(lambda: collections.defaultdict(int))
        result = prefix = prefix2 = 0
        for i in range(len(capacity)):
            result += cnt[capacity[i]][prefix-capacity[i]]
            prefix += capacity[i]
            if (i+1)-L+1 >= 0:
                prefix2 += capacity[(i+1)-L+1]
                cnt[capacity[(i+1)-L+1]][prefix2] += 1
        return result


