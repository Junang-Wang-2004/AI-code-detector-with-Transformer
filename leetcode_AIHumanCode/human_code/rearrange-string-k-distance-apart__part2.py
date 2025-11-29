# Time:  O(n)
# Space: O(n)
import collections
import itertools


# reference: https://codeforces.com/blog/entry/110184 1774B - Coloring
class Solution2(object):
    def rearrangeString(self, s, k):
        """
        """
        if not k:
            return s
        cnts = collections.Counter(s)
        bucket_cnt = (len(s)+k-1)//k
        if not (max(cnts.values()) <= bucket_cnt and list(cnts.values()).count(bucket_cnt) <= (len(s)-1)%k+1):
            return ""
        result = [0]*len(s)
        i = 0
        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt),
                                 (c for c, v in cnts.items() if v <= bucket_cnt-2),
                                 (c for c, v in cnts.items() if v == bucket_cnt-1)):
            for _ in range(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = i%k+1
        return "".join(result)


