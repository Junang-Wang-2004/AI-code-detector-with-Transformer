from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        n = len(chargeTimes)
        max_length = 0
        window_sum = 0
        left = 0
        max_deque = deque()
        for right in range(n):
            while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
                max_deque.pop()
            max_deque.append(right)
            window_sum += runningCosts[right]
            while left <= right and chargeTimes[max_deque[0]] + (right - left + 1) * window_sum > budget:
                window_sum -= runningCosts[left]
                left += 1
                while max_deque and max_deque[0] < left:
                    max_deque.popleft()
            max_length = max(max_length, right - left + 1)
        return max_length
