# Time:  O(nlogn)
# Space: O(1)

# greedy
class Solution(object):
    def minimumCost(self, cost):
        """
        """
        cost.sort(reverse=True)
        return sum(x for i, x in enumerate(cost) if i%3 != 2)
