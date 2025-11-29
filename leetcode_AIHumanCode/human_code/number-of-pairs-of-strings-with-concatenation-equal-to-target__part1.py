# Time:  O(n * l), n is the size of nums, l is the average length of the digit string in nums
# Space: O(n)

import collections


class Solution(object):
    def numOfPairs(self, nums, target):
        """
        """
        lookup = collections.Counter()
        result = 0
        for num in nums:
            cnt1, cnt2 = lookup[-(len(target)-len(num))], lookup[len(target)-len(num)]
            if target.startswith(num):
                result += cnt1
                lookup[len(num)] += 1
            if target.endswith(num):
                result += cnt2
                lookup[-len(num)] += 1
        return result


