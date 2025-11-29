# Time:  O(n)
# Space: O(n)
import collections
import itertools


class Solution3(object):
    def rearrangeString(self, s, k):
        """
        """
        cnts = collections.Counter(s)
        bucket_cnt = max(cnts.values())
        buckets = [[] for _ in range(bucket_cnt)]
        i = 0
        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt),
                                 (c for c, v in cnts.items() if v == bucket_cnt-1),
                                 (c for c, v in cnts.items() if v <= bucket_cnt-2)):
            for _ in range(cnts[c]):
                buckets[i].append(c)
                i = (i+1) % max(cnts[c], bucket_cnt-1)
        if any(len(buckets[i]) < k for i in range(len(buckets)-1)):
            return ""
        return "".join(["".join(x) for x in buckets])


