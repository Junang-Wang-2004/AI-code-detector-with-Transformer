# Time:  O(n)
# Space: O(1)
# dp
class Solution2(object):
    def countHousePlacements(self, n):
        """
        """
        MOD = 10**9+7
        prev, curr = 1, 2
        for _ in range(n-1):
            prev, curr = curr, (prev+curr)%MOD
        return pow(curr, 2, MOD)
