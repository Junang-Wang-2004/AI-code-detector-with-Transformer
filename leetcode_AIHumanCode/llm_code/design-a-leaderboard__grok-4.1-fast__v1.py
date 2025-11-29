class Leaderboard:

    def __init__(self):
        self.player_totals = {}

    def addScore(self, iden, points):
        self.player_totals[iden] = self.player_totals.get(iden, 0) + points

    def top(self, K):
        all_scores = sorted(self.player_totals.values(), reverse=True)
        total = 0
        for i in range(K):
            if i < len(all_scores):
                total += all_scores[i]
        return total

    def reset(self, iden):
        self.player_totals[iden] = 0
