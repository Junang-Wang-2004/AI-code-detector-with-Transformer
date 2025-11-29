# Time:  O(n * m * (logn + logr)), r = max(nums)
# Space: O(n + logr)
# dp, sparse table
class Solution2(object):
    def minimumValueSum(self, nums, andValues):
        """
        """
        INF = float("inf")
        # RMQ - Sparse Table
        # Template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20D/genetic_sequences2.py3
