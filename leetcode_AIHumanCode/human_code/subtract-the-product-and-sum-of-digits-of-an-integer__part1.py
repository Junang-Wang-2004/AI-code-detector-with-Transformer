# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        """
        product, total = 1, 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            total += r
        return product-total


