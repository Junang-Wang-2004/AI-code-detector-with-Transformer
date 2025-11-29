# Time:  O(n * llogl)
# Space: O(l)
import collections


# sort
class Solution2(object):
    def removeAnagrams(self, words):
        """
        """
        result = []
        prev = None
        for x in words:
            s = sorted(x)
            if prev and prev == s:
                continue
            prev = s
            result.append(x)
        return result


