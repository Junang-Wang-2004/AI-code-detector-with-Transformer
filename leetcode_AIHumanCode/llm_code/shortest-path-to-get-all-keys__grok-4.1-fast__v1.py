import collections
import heapq

class Solution(object):
    def shortestPathAllKeys(self, grid):
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        special_pos = {}
        for row in range(grid_rows):
            for col in range(grid_cols):
                ch = grid[row][col]
                if ch != '.' and ch != '#':
                    special_pos[ch] = (row, col)
        def get_dists(grid, special_pos, grid_rows, grid_cols, dirs):
            path_dists = {src: {} for src in special_pos}
            for src in special_pos:
                sr, sc = special_pos[src]
                visited = [[False] * grid_cols for _ in range(grid_rows)]
                visited[sr][sc] = True
                que = collections.deque([(sr, sc, 0)])
                while que:
                    cr, cc, steps = que.popleft()
                    curr_ch = grid[cr][cc]
                    if curr_ch != '.' and curr_ch != '#' and curr_ch != src:
                        path_dists[src][curr_ch] = steps
                        continue
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < grid_rows and 0 <= nc < grid_cols and grid[nr][nc] != '#' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            que.append((nr, nc, steps + 1))
            return path_dists
        dists = get_dists(grid, special_pos, grid_rows, grid_cols, dirs)
        full_mask = 0
        for ch in special_pos:
            if ch.islower():
                full_mask |= 1 << (ord(ch) - ord('a'))
        start_pos = '@'
        pq = []
        heapq.heappush(pq, (0, 0, start_pos))
        min_dist = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        min_dist[start_pos][0] = 0
        while pq:
            total_steps, key_mask, curr_pos = heapq.heappop(pq)
            if total_steps > min_dist[curr_pos][key_mask]:
                continue
            if key_mask == full_mask:
                return total_steps
            for next_loc, move_cost in dists[curr_pos].items():
                new_key_mask = key_mask
                if next_loc.islower():
                    bit_pos = ord(next_loc) - ord('a')
                    new_key_mask |= 1 << bit_pos
                elif next_loc.isupper():
                    req_bit = ord(next_loc) - ord('A')
                    if not (key_mask & (1 << req_bit)):
                        continue
                cand_dist = total_steps + move_cost
                if cand_dist < min_dist[next_loc][new_key_mask]:
                    min_dist[next_loc][new_key_mask] = cand_dist
                    heapq.heappush(pq, (cand_dist, new_key_mask, next_loc))
        return -1
