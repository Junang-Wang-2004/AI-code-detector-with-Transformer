class C1:

    def __init__(self):
        self.player_totals = {}

    def addScore(self, a1, a2):
        self.player_totals[a1] = self.player_totals.get(a1, 0) + a2

    def top(self, a1):
        v1 = sorted(self.player_totals.values(), reverse=True)
        v2 = 0
        for v3 in range(a1):
            if v3 < len(v1):
                v2 += v1[v3]
        return v2

    def reset(self, a1):
        self.player_totals[a1] = 0
