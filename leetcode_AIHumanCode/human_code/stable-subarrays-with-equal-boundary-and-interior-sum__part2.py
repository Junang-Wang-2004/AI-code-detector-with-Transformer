# Time:  O(n)
# Space: O(n)
import collections


# freq table, prefix sum
class Solution2(object):
    def countStableSubarrays(self, capacity):
        """
        """
        cnt = collections.defaultdict(lambda: collections.defaultdict(int))
        result = prefix = 0
        for i, x in enumerate(capacity):
            result += cnt[x][prefix-x]
            prefix += x
            cnt[x][prefix] += 1
            if x == 0 and i-1 >= 0 and capacity[i-1] == 0:
                result -= 1
        return result
