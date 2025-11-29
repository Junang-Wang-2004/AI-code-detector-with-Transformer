from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = deque([''])
        for num in digits:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                for char in mapping[num]:
                    queue.append(current + char)
        return list(queue)
