# Time:  O((n + k) * logn)
# Space: O(nlogn)
import heapq


# heap, rmq, sparse table
class Solution2(object):
    def maxTotalValue(self, nums, k):
        """
        """
        # RMQ - Sparse Table
        # Template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20D/genetic_sequences2.py3
