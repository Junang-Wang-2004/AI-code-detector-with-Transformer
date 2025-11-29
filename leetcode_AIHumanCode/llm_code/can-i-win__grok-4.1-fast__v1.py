class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        m = maxChoosableInteger
        if m * (m + 1) // 2 < desiredTotal:
            return False

        memo = {}

        def player_can_force_win(remaining, state):
            if state in memo:
                return memo[state]

            for idx in range(m - 1, -1, -1):
                bit_pos = 1 << idx
                if (state & bit_pos) == 0:
                    choice = idx + 1
                    next_remaining = remaining - choice
                    next_state = state | bit_pos
                    if choice >= remaining or not player_can_force_win(next_remaining, next_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return player_can_force_win(desiredTotal, 0)
