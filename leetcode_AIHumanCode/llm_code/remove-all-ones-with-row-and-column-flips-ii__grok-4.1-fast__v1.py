class Solution:
    def removeOnes(self, grid):
        rows, c = len(grid), len(grid[0])
        positions = rows * c
        state_mask = 0
        row_masks = [0] * rows
        col_masks = [0] * c
        for i in range(rows):
            for j in range(c):
                if grid[i][j]:
                    pos = i * c + j
                    bit = 1 << pos
                    state_mask |= bit
                    row_masks[i] |= bit
                    col_masks[j] |= bit
        if state_mask == 0:
            return 0
        operations = []
        for i in range(rows):
            for j in range(c):
                if grid[i][j]:
                    operations.append(row_masks[i] | col_masks[j])
        INF = float('inf')
        memo = [INF] * (state_mask + 1)
        memo[0] = 0
        for current in range(state_mask + 1):
            if memo[current] == INF:
                continue
            for op_mask in operations:
                next_state = current | op_mask
                memo[next_state] = min(memo[next_state], memo[current] + 1)
        return memo[state_mask]
