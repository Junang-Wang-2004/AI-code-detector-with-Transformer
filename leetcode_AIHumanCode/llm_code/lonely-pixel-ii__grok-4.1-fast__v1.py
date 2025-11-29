class Solution(object):
    def findBlackPixel(self, picture, N):
        m, n = len(picture), len(picture[0]) if picture else 0
        if m == 0 or n == 0:
            return 0
        col_blacks = [0] * n
        for r in picture:
            for j, c in enumerate(r):
                if c == 'B':
                    col_blacks[j] += 1
        row_stats = {}
        for entire_row in picture:
            if entire_row not in row_stats:
                row_stats[entire_row] = [0, entire_row.count('B')]
            row_stats[entire_row][0] += 1
        total_valid = 0
        for entire_row, (occurrences, num_blacks) in row_stats.items():
            if occurrences == N and num_blacks == N:
                valid_per_row = 0
                for j in range(n):
                    if entire_row[j] == 'B' and col_blacks[j] == N:
                        valid_per_row += 1
                total_valid += valid_per_row * N
        return total_valid
