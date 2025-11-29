# Time:  O(n * a)
# Space: O(n)
import collections


# optimized from Solution5
class Solution3(object):
    def bestTeamScore(self, scores, ages):
        """
        """
        players = sorted(zip(scores, ages))
        sorted_ages = sorted(set(ages))
        dp = collections.defaultdict(int)
        result = 0
        for score, age in players:
            dp[age] = max(dp[a] for a in sorted_ages if a <= age) + score
        return max(dp.values())


