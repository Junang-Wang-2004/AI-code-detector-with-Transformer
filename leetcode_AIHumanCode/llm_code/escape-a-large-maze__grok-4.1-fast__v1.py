class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        SZ = 1000000
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def reachable(hurdles, start_pos, finish_pos):
            hurdle_set = set(tuple(pos) for pos in hurdles)
            num_hurdles = len(hurdle_set)
            max_enclosed = num_hurdles * (num_hurdles - 1) // 2
            visited_set = set([start_pos])
            if len(visited_set) > max_enclosed:
                return True
            bfs_queue = [start_pos]
            while bfs_queue:
                curr_pos = bfs_queue.pop(0)
                if curr_pos == finish_pos:
                    return True
                for dr, dc in moves:
                    next_r = curr_pos[0] + dr
                    next_c = curr_pos[1] + dc
                    next_pos = (next_r, next_c)
                    if (0 <= next_r < SZ and 0 <= next_c < SZ and
                        next_pos not in visited_set and next_pos not in hurdle_set):
                        visited_set.add(next_pos)
                        if len(visited_set) > max_enclosed:
                            return True
                        bfs_queue.append(next_pos)
            return False

        obs_set = set(tuple(cell) for cell in blocked)
        src = tuple(source)
        dst = tuple(target)
        return reachable(obs_set, src, dst) and reachable(obs_set, dst, src)
