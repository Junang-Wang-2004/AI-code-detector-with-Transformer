from collections import deque

class Solution:
    def maxHammingDistances(self, nums, m):
        size = 1 << m
        distances = [-1] * size
        queue = deque()
        visited = set()
        all_ones = size - 1
        for val in nums:
            if val not in visited:
                visited.add(val)
                distances[val] = 0
                queue.append(val)
        while queue:
            current = queue.popleft()
            for bit in range(m):
                neighbor = current ^ (1 << bit)
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        result = []
        for val in nums:
            complement = all_ones ^ val
            result.append(m - distances[complement])
        return result
