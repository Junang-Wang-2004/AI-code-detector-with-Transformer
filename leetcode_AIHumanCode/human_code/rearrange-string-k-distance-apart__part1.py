# Time:  O(n)
# Space: O(c)

import collections
import itertools


class Solution(object):
    def rearrangeString(self, s, k):
        """
        """
        if not k:
            return s
        cnts = collections.Counter(s)
        bucket_cnt = max(cnts.values())
        if not ((bucket_cnt-1)*k+sum(x == bucket_cnt for x in cnts.values()) <= len(s)):
            return ""
        result = [0]*len(s)
        i = (len(s)-1)%k
        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):
            for _ in range(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = (i-1)%k
        return "".join(result)


