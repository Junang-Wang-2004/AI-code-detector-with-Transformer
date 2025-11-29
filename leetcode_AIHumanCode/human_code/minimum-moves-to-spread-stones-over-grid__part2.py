# Time:  O(max(x^2 * y)) = O(n^2), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# Space: O(max(x^2)) = O(n^2)
from scipy.optimize import linear_sum_assignment as hungarian
import itertools


# 3rd-party weighted bipartite matching solution
class Solution2(object):
    def minimumMoves(self, grid):
        """
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        src, dst = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]-1 >= 0:
                    src.extend([(i, j)]*(grid[i][j]-1))
                else:
                    dst.append((i, j))
        adj = [[dist(src[i], dst[j]) for j in range(len(dst))] for i in range(len(src))]
        return sum(adj[i][j] for i, j in zip(*hungarian(adj)))    


