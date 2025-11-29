# Time:  O(n), k is the number of distinct barcodes
# Space: O(k)

import collections
import itertools


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        """
        k = 2
        cnts = collections.Counter(barcodes)
        bucket_cnt = max(cnts.values())
        result = [0]*len(barcodes)
        i = (len(barcodes)-1)%k
        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):
            for _ in range(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = (i-1)%k
        return result

    
