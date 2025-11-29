from collections import deque

class Solution(object):
    def countSteppingNumbers(self, low, high):
        ans = []
        seen = set()
        queue = deque()
        for digit in range(10):
            if digit <= high:
                queue.append(digit)
                seen.add(digit)
        while queue:
            current = queue.popleft()
            if current >= low:
                ans.append(current)
            prev_digit = current % 10
            for diff in (-1, 1):
                next_digit = prev_digit + diff
                if 0 <= next_digit <= 9:
                    next_val = current * 10 + next_digit
                    if next_val <= high and next_val not in seen:
                        seen.add(next_val)
                        queue.append(next_val)
        return ans
