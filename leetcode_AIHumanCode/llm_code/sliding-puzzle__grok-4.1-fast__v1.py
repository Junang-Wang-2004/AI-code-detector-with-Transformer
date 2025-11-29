import collections

class Solution:
    def slidingPuzzle(self, board):
        rows, cols = len(board), len(board[0])
        size = rows * cols
        goal = tuple(range(1, size)) + (0,)
        initial = tuple(b for row in board for b in row)
        if initial == goal:
            return 0
        seen = {initial}
        queue = collections.deque([(initial, 0)])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            current, steps = queue.popleft()
            blank = current.index(0)
            br, bc = divmod(blank, cols)
            for dr, dc in moves:
                nr, nc = br + dr, bc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    swap_pos = nr * cols + nc
                    state_list = list(current)
                    state_list[blank], state_list[swap_pos] = state_list[swap_pos], state_list[blank]
                    new_state = tuple(state_list)
                    if new_state not in seen:
                        if new_state == goal:
                            return steps + 1
                        seen.add(new_state)
                        queue.append((new_state, steps + 1))
        return -1
