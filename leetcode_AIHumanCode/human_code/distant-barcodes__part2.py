# Time:  O(n + klogk), k is the number of distinct barcodes
# Space: O(k)
import collections


class Solution2(object):
    def rearrangeBarcodes(self, barcodes):
        """
        """
        cnts = collections.Counter(barcodes)
        sorted_cnts = [[v, k] for k, v in cnts.items()]
        sorted_cnts.sort(reverse=True)

        i = 0
        for v, k in sorted_cnts:
            for _ in range(v):
                barcodes[i] = k
                i += 2
                if i >= len(barcodes):
                    i = 1
        return barcodes
