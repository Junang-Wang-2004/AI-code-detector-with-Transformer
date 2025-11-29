# Time:  O(n^3)
# Space: O(n^2)
from scipy.optimize import linear_sum_assignment as hungarian
import itertools


# 3rd-party weighted bipartite matching solution
class Solution2(object):
    def maximumANDSum(self, nums, numSlots):
        """
        """
        adj = [[-((nums[i] if i < len(nums) else 0) & (1+x//2)) for x in range(2*numSlots)] for i in range(2*numSlots)]
        return -sum(adj[i][j] for i, j in zip(*hungarian(adj)))    


