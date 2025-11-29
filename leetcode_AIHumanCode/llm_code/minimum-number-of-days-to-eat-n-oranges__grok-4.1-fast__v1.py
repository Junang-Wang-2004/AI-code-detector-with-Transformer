from collections import deque

class Solution:
    def minDays(self, n):
        if n == 0:
            return 0
        memo = {}
        queue = deque([n])
        memo[n] = 0
        while queue:
            current = queue.popleft()
            if current == 0:
                return memo[current]
            prev = current - 1
            if prev >= 0 and prev not in memo:
                memo[prev] = memo[current] + 1
                queue.append(prev)
            if current % 2 == 0:
                half = current // 2
                if half not in memo:
                    memo[half] = memo[current] + 1
                    queue.append(half)
            if current % 3 == 0:
                third = current // 3
                if third not in memo:
                    memo[third] = memo[current] + 1
                    queue.append(third)
