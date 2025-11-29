# Time:  O(m * 2^n * 2^n) = O(m * 4^n)
# Space: O(2^n)
# dp solution
class Solution3(object):
    def maxStudents(self, seats):
        """
        """
        def popcount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result
        
        dp = {0: 0}
        for row in seats:
            invalid_mask = sum(1 << c for c, v in enumerate(row) if v == '#')
            new_dp = {}
            for mask1, v1 in dp.items():
                for mask2 in range(1 << len(seats[0])):
                    if (mask2 & invalid_mask) or \
                       (mask2 & (mask1 << 1)) or (mask2 & (mask1 >> 1)) or \
                       (mask2 & (mask2 << 1)) or (mask2 & (mask2 >> 1)):
                        continue
                    new_dp[mask2] = max(new_dp.get(mask2, 0), v1+popcount(mask2))
            dp = new_dp
        return max(dp.values()) if dp else 0
