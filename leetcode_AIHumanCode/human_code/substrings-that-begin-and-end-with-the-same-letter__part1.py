# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        """
        result = 0
        cnt = collections.Counter()
        for c in s:
            cnt[c] += 1
            result += cnt[c]
        return result


