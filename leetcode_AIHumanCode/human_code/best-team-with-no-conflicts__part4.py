# Time:  O(n * s)
# Space: O(n)
import collections


# optimized from Solution6
class Solution4(object):
    def bestTeamScore(self, scores, ages):
        """
        """
        players = sorted(zip(ages, scores))
        sorted_scores = sorted(set(scores))
        dp = collections.defaultdict(int)
        result = 0
        for age, score in players:
            dp[score] = max(dp[s] for s in sorted_scores if s <= score) + score
        return max(dp.values())


