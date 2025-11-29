from collections import deque

class Solution:
    def racecar(self, target):
        q = deque([(0, 1, 0)])
        vis = {(0, 1)}
        while q:
            pos, spd, moves = q.popleft()
            if pos == target:
                return moves
            for delta, new_spd in [(spd, spd * 2), (0, -spd)]:
                new_pos = pos + delta
                state = (new_pos, new_spd)
                if state not in vis and abs(new_pos) <= target * 2:
                    vis.add(state)
                    q.append((new_pos, new_spd, moves + 1))
