# Time:  O(n)
# Space: O(1)

import collections
import string


class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        """
        def is_break(count1, count2):
            curr1, curr2 = 0, 0
            for c in string.ascii_lowercase:
                curr1 += count1[c]
                curr2 += count2[c]
                if curr1 < curr2:
                    return False
            return True

        count1, count2 = collections.Counter(s1), collections.Counter(s2)
        return is_break(count1, count2) or is_break(count2, count1)
    

