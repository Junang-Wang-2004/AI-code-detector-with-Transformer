from collections import deque

class Solution:
    def openLock(self, deadends, target):
        forbidden = set(deadends)
        visited = set(forbidden)
        if "0000" in visited:
            return -1
        q = deque([("0000", 0)])
        visited.add("0000")
        while q:
            state, dist = q.popleft()
            if state == target:
                return dist
            for wheel in range(4):
                orig_digit = int(state[wheel])
                for change in (-1, 1):
                    new_digit = (orig_digit + change) % 10
                    next_state = state[:wheel] + str(new_digit) + state[wheel + 1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        q.append((next_state, dist + 1))
        return -1
