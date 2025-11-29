# Time:  O(n)
# Space: O(n)
import collections


# freq table, constructive algorithms
class Solution2(object):
    def findMatrix(self, nums):
        """
        """
        result = []
        cnt = collections.Counter(nums)
        while cnt:
            result.append(list(cnt.keys()))
            cnt = {k:v-1 for k, v in cnt.items() if v-1}
        return result
