class Solution(object):
    def findWinners(self, matches):
        losses = {}
        appearances = []
        for victor, defeated in matches:
            losses[defeated] = losses.get(defeated, 0) + 1
            appearances.extend([victor, defeated])
        sorted_players = sorted(set(appearances))
        undefeated = []
        single_loss = []
        for player in sorted_players:
            loss_num = losses.get(player, 0)
            if loss_num == 0:
                undefeated.append(player)
            elif loss_num == 1:
                single_loss.append(player)
        return [undefeated, single_loss]
