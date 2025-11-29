# Time:  O(n)
# Space: O(1)
import collections


class Solution2(object):
    def sortString(self, s):
        """
        """
        result, count, desc = [], collections.Counter(s), False
        while count:
            for c in sorted(list(count.keys()), reverse=desc):
                result.append(c)
                count[c] -= 1
                if not count[c]:
                    del count[c]
            desc = not desc
        return "".join(result)

