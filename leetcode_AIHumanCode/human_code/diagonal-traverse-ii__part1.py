# Time:  O(m * n)
# Space: O(m)

import itertools
import collections


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        """
        result, dq, col = [], collections.deque(), 0
        for i in range(len(nums)+max(map(len, nums))-1):
            new_dq = collections.deque()
            if i < len(nums):
                dq.appendleft((i, 0))
            for r, c in dq:
                result.append(nums[r][c])
                if c+1 < len(nums[r]):
                    new_dq.append((r, c+1))
            dq = new_dq
        return result


