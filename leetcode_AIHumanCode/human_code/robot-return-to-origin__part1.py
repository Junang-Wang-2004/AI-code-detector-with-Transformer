# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def judgeCircle(self, moves):
        """
        """
        count = collections.Counter(moves)
        return count['L'] == count['R'] and count['U'] == count['D']

 
