# Time:  O(n)
# Space: O(n)

import collections


# freq table, constructive algorithms
class Solution(object):
    def findMatrix(self, nums):
        """
        """
        result = []
        cnt = collections.Counter()
        for x in nums:
            if cnt[x] == len(result):
                result.append([])
            result[cnt[x]].append(x)
            cnt[x] += 1
        return result


