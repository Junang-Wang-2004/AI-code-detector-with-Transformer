# Time:  O(n * m * log(max(n, m)) + max(n, m)^2)
# Space: O(n * m * log(max(n, m)))
# sparse table
class Solution3(object):
    def minimumSum(self, grid):
        """
        """
        # RMQ - Sparse Table
        # Template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20D/genetic_sequences2.py3
