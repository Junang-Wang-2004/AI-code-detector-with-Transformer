from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        window = deque([0])
        for curr in range(1, n):
            while window and window[0] < curr - maxJump:
                window.popleft()
            can_land = s[curr] == '0' and window and window[0] <= curr - minJump
            if can_land:
                window.append(curr)
        return bool(window) and window[-1] == n - 1
