class Solution(object):
    def winnerOfGame(self, colors):
        moves_a = 0
        moves_b = 0
        n = len(colors)
        i = 0
        while i < n:
            start = i
            while i < n and colors[i] == colors[start]:
                i += 1
            run_len = i - start
            if run_len >= 3:
                if colors[start] == 'A':
                    moves_a += run_len - 2
                else:
                    moves_b += run_len - 2
        return moves_a > moves_b
