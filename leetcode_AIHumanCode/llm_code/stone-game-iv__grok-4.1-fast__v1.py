class Solution:
    def winnerSquareGame(self, n):
        can_win = [False] * (n + 1)
        max_side = int(n ** 0.5) + 1
        for side in range(1, max_side + 1):
            sq_size = side * side
            for pos in range(sq_size, n + 1):
                if not can_win[pos - sq_size]:
                    can_win[pos] = True
        return can_win[n]
