class Solution(object):
    def minMoves(self, classroom, energy):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(classroom)
        cols = len(classroom[0])
        sr = sc = None
        lamp_positions = []
        for i in range(rows):
            for j in range(cols):
                ch = classroom[i][j]
                if ch == 'S':
                    sr, sc = i, j
                elif ch == 'L':
                    lamp_positions.append((i, j))
        num_lamps = len(lamp_positions)
        target_mask = (1 << num_lamps) - 1
        lamp_bitpos = [[-1] * cols for _ in range(rows)]
        for bit, (x, y) in enumerate(lamp_positions):
            lamp_bitpos[x][y] = bit
        reach_energy = [[[-1] * (1 << num_lamps) for _ in range(cols)] for _ in range(rows)]
        reach_energy[sr][sc][0] = energy
        current_queue = [(sr, sc, 0, energy)]
        steps = 0
        while current_queue:
            next_queue = []
            for r, c, mask, e in current_queue:
                if reach_energy[r][c][mask] != e:
                    continue
                if mask == target_mask:
                    return steps
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    next_e = e - 1
                    if not (0 <= nr < rows and 0 <= nc < cols and
                            classroom[nr][nc] != 'X' and next_e >= 0):
                        continue
                    next_mask = mask
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                    bit = lamp_bitpos[nr][nc]
                    if bit != -1:
                        next_mask |= (1 << bit)
                    if next_e > reach_energy[nr][nc][next_mask]:
                        reach_energy[nr][nc][next_mask] = next_e
                        next_queue.append((nr, nc, next_mask, next_e))
            current_queue = next_queue
            steps += 1
        return -1
