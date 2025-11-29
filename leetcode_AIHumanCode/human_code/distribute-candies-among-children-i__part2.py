# Time:  O(n)
# Space: O(1)
# optimized brute force
class Solution2(object):
    def distributeCandies(self, n, limit):
        """
        """
        return sum(min(limit, n-i)-max((n-i)-limit, 0)+1 for i in range(max(n-2*limit, 0), min(limit, n)+1))


