# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        """
        def boyer_moore_majority_vote():
            result, cnt = None, 0
            for x in nums:
                if not cnt:
                    result = x
                if x == result:
                    cnt += 1
                else:
                    cnt -= 1
            return result

        return boyer_moore_majority_vote()


