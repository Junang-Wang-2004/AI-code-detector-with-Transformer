# Time:  O(52n)
# Space: O(52)
class Solution2(object):
    def minimumDistance(self, word):
        """
        """
        def distance(a, b):
            if -1 in [a, b]:
                return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = {(-1, -1): 0}
        for c in word:
            c = ord(c)-ord('A')
            new_dp = {}
            for a, b in dp:
                new_dp[c, b] = min(new_dp.get((c, b), float("inf")), dp[a, b] + distance(a, c))
                new_dp[a, c] = min(new_dp.get((a, c), float("inf")), dp[a, b] + distance(b, c))
            dp = new_dp
        return min(dp.values())
