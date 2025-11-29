from functools import reduce
# Time:  O(n)
# Space: O(1)

# bottom-up solution
class Solution(object):
    def findTheWinner(self, n, k):
        """
        """
        return reduce(lambda idx, n:(idx+k)%(n+1), range(1, n), 0)+1


