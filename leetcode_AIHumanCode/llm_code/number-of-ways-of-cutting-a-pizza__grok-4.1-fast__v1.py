class Solution:
    def ways(self, pizza, k):
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        suffix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                suffix[r][c] = suffix[r][c + 1] + suffix[r + 1][c] - suffix[r + 1][c + 1] + (1 if pizza[r][c] == 'A' else 0)
        memo = [[[-1] * k for _ in range(cols)] for _ in range(rows)]

        def count_ways(start_row, start_col, cuts_left):
            if cuts_left == 0:
                return 1 if suffix[start_row][start_col] > 0 else 0
            if memo[start_row][start_col][cuts_left] != -1:
                return memo[start_row][start_col][cuts_left]
            result = 0
            for next_row in range(start_row + 1, rows):
                if suffix[start_row][start_col] > suffix[next_row][start_col]:
                    result = (result + count_ways(next_row, start_col, cuts_left - 1)) % MOD
                if suffix[next_row][start_col] == 0:
                    break
            for next_col in range(start_col + 1, cols):
                if suffix[start_row][start_col] > suffix[start_row][next_col]:
                    result = (result + count_ways(start_row, next_col, cuts_left - 1)) % MOD
                if suffix[start_row][next_col] == 0:
                    break
            memo[start_row][start_col][cuts_left] = result
            return result

        return count_ways(0, 0, k - 1)
