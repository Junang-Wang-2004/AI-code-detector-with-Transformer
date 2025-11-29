# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution3(object):
    def distributeCandies(self, n, limit):
        """
        """
        return sum(n-i-j <= limit for i in range(min(limit, n)+1) for j in range(min(limit, n-i)+1))
