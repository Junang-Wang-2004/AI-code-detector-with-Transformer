from collections import deque

class Solution:
    def minimumOperations(self, nums, start, goal):
        if start == goal:
            return 0
        MAX_VAL = 1000
        dist = [-1] * (MAX_VAL + 1)
        dist[start] = 0
        queue = deque([start])
        allowed = list({num for num in nums if num})
        while queue:
            current = queue.popleft()
            depth = dist[current]
            for num in allowed:
                candidates = [current + num, current - num, current ^ num]
                for candidate in candidates:
                    if 0 <= candidate <= MAX_VAL and dist[candidate] == -1:
                        dist[candidate] = depth + 1
                        if candidate == goal:
                            return depth + 1
                        queue.append(candidate)
        return -1
