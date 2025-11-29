from functools import reduce
# Time:  O(n * k)
# Space: O(k)

class Solution2(object):
    def minCostII(self, costs):
        """
        """
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])
        min_cost = [costs[0], [0] * k]
        for i in range(1, n):
            smallest, second_smallest = float("inf"), float("inf")
            for j in range(k):
                if min_cost[(i - 1) % 2][j] < smallest:
                    smallest, second_smallest = min_cost[(i - 1) % 2][j], smallest
                elif min_cost[(i - 1) % 2][j] < second_smallest:
                    second_smallest = min_cost[(i - 1) % 2][j]
            for j in range(k):
                min_j = smallest if min_cost[(i - 1) % 2][j] != smallest else second_smallest
                min_cost[i % 2][j] = costs[i][j] + min_j

        return min(min_cost[(n - 1) % 2])

