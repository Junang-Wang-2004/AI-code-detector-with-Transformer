class Solution(object):
    def isWinner(self, teamA, teamB):
        def get_score(points):
            total = 0
            n = len(points)
            for idx in range(n):
                multiplier = 1
                if idx > 0 and points[idx - 1] == 10:
                    multiplier = 2
                if idx > 1 and points[idx - 2] == 10:
                    multiplier = 2
                total += points[idx] * multiplier
            return total

        scoreA = get_score(teamA)
        scoreB = get_score(teamB)
        if scoreA > scoreB:
            return 1
        return 2 if scoreA < scoreB else 0
