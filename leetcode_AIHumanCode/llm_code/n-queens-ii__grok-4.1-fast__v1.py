class Solution:
    def totalNQueens(self, n):
        def search(level, placement):
            if level == n:
                return 1
            ways = 0
            for position in range(n):
                if safe(placement, level, position):
                    placement[level] = position
                    ways += search(level + 1, placement)
            return ways

        def safe(placement, level, position):
            for prior in range(level):
                prior_pos = placement[prior]
                if prior_pos == position or abs(prior - level) == abs(prior_pos - position):
                    return False
            return True

        placement = [-1] * n
        return search(0, placement)
