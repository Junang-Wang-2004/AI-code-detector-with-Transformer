class Solution(object):
    def distributeCandies(self, n, limit):
        """
        """
        L = limit + 1
        
        def count_ways(m):
            return 0 if m < 0 else (m + 1) * (m + 2) // 2
        
        unrestricted = count_ways(n)
        one_excess = 3 * count_ways(n - L)
        two_excess = 3 * count_ways(n - 2 * L)
        three_excess = count_ways(n - 3 * L)
        
        return unrestricted - one_excess + two_excess - three_excess
