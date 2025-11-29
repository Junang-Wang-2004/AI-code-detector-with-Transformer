import sys
sys.setrecursionlimit(10**6)

class Solution:
    def minimumOperations(self, grid):
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        even_positions = []
        odd_positions = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    pos = i * cols + j
                    if (i + j) % 2 == 0:
                        even_positions.append(pos)
                    else:
                        odd_positions.append(pos)
        side_u = even_positions if len(even_positions) <= len(odd_positions) else odd_positions
        side_v = odd_positions if len(even_positions) <= len(odd_positions) else even_positions
        num_u = len(side_u)
        num_v = len(side_v)
        if num_u == 0:
            return 0
        v_to_idx = {side_v[k]: k for k in range(num_v)}
        adj_list = [[] for _ in range(num_u)]
        for u_id in range(num_u):
            u_pos = side_u[u_id]
            u_row, u_col = divmod(u_pos, cols)
            for dr, dc in directions:
                v_row = u_row + dr
                v_col = u_col + dc
                if 0 <= v_row < rows and 0 <= v_col < cols and grid[v_row][v_col] == 1:
                    v_pos = v_row * cols + v_col
                    if v_pos in v_to_idx:
                        adj_list[u_id].append(v_to_idx[v_pos])
        match_u = [-1] * num_u
        match_v = [-1] * num_v

        def try_augment(u, vis):
            for v in adj_list[u]:
                if vis[v]:
                    continue
                vis[v] = True
                if match_v[v] == -1 or try_augment(match_v[v], vis):
                    match_u[u] = v
                    match_v[v] = u
                    return True
            return False

        total_matching = 0
        progress = True
        while progress:
            progress = False
            vis = [False] * num_v
            for u in range(num_u):
                if match_u[u] == -1 and try_augment(u, vis):
                    total_matching += 1
                    progress = True
        return total_matching
