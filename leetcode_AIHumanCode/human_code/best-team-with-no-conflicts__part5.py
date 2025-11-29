# Time:  O(n^2)
# Space: O(n)
# longest_increasing_subsequence like dp solution
class Solution5(object):
    def bestTeamScore(self, scores, ages):
        """
        """
        players = sorted(zip(scores, ages))
        dp = [0]*len(players)
        result = 0
        for i in range(len(players)):
            dp[i] = players[i][0]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][0])
            result = max(result, dp[i])
        return result


