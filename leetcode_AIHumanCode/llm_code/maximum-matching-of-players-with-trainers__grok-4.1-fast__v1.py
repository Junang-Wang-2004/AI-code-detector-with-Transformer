class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        i, j = 0, 0
        pairs = 0
        lp, lt = len(players), len(trainers)
        while i < lp and j < lt:
            if players[i] <= trainers[j]:
                pairs += 1
                i += 1
                j += 1
            else:
                j += 1
        return pairs
