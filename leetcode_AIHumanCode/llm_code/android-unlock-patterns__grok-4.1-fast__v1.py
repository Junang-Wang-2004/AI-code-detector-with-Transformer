class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        SIZE = 1 << 9
        popcount = [bin(i).count('1') for i in range(SIZE)]
        visited = [[-1] * SIZE for _ in range(9)]

        def count_ways(current: int, state: int) -> int:
            if visited[current][state] >= 0:
                return visited[current][state]
            len_path = popcount[state]
            ways = 1 if m <= len_path <= n else 0
            if len_path == n:
                visited[current][state] = ways
                return ways
            row_from, col_from = divmod(current, 3)
            for next_pos in range(9):
                if (state & (1 << next_pos)) == 0:
                    row_to, col_to = divmod(next_pos, 3)
                    delta_row = abs(row_from - row_to)
                    delta_col = abs(col_from - col_to)
                    can_jump = True
                    if (delta_row == 2 and delta_col == 0) or (delta_row == 0 and delta_col == 2) or (delta_row == 2 and delta_col == 2):
                        mid_row = (row_from + row_to) // 2
                        mid_col = (col_from + col_to) // 2
                        mid_pos = mid_row * 3 + mid_col
                        if (state & (1 << mid_pos)) == 0:
                            can_jump = False
                    if can_jump:
                        new_state = state | (1 << next_pos)
                        ways += count_ways(next_pos, new_state)
            visited[current][state] = ways
            return ways

        result = 0
        for initial in range(9):
            result += count_ways(initial, 1 << initial)
        return result
