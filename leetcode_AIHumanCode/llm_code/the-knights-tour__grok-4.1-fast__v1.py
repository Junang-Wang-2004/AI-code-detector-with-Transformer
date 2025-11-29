class Solution:
    def tourOfKnight(self, m, n, row_start, col_start):
        tour_board = [[-1] * n for _ in range(m)]
        tour_board[row_start][col_start] = 0
        knight_deltas = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        def get_valid_moves(r, c):
            valid_next = []
            for delta_r, delta_c in knight_deltas:
                new_r = r + delta_r
                new_c = c + delta_c
                if 0 <= new_r < m and 0 <= new_c < n and tour_board[new_r][new_c] == -1:
                    valid_next.append((new_r, new_c))
            return valid_next
        def find_path(curr_r, curr_c, step_count):
            if step_count == m * n:
                return True
            next_positions = get_valid_moves(curr_r, curr_c)
            next_positions.sort(key=lambda pos: len(get_valid_moves(pos[0], pos[1])))
            for next_r, next_c in next_positions:
                tour_board[next_r][next_c] = step_count
                if find_path(next_r, next_c, step_count + 1):
                    return True
                tour_board[next_r][next_c] = -1
            return False
        find_path(row_start, col_start, 1)
        return tour_board
