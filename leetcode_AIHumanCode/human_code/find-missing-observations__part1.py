# Time:  O(n)
# Space: O(1)

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        """
        MAX_V = 6
        MIN_V = 1
        total = sum(rolls)
        missing = mean*(n+len(rolls))-total
        if missing < MIN_V*n or missing > MAX_V*n:
            return []
        q, r = divmod(missing, n)
        return [q+int(i < r) for i in range(n)]


