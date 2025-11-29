# Time:  O(n * l)
# Space: O(1)

import collections


# freq table
class Solution(object):
    def removeAnagrams(self, words):
        """
        """
        result = []
        prev = None
        for x in words:
            cnt = collections.Counter(x)
            if prev and prev == cnt:
                continue
            prev = cnt
            result.append(x)
        return result


