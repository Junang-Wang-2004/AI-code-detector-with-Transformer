# Time:  O(n * d * l), l is the average string length
# Space: O(n)

import collections
import functools


# 59ms
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        """
        lookup = [0] * len(s)
        for d in dict:
            pos = s.find(d)
            while pos != -1:
                lookup[pos:pos+len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)


