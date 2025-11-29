from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = deque([(root, 0)])
        result = 0
        while queue:
            level_length = len(queue)
            min_index = float('inf')
            max_index = float('-inf')
            for _ in range(level_length):
                current, position = queue.popleft()
                min_index = min(min_index, position)
                max_index = max(max_index, position)
                if current.left:
                    queue.append((current.left, position * 2))
                if current.right:
                    queue.append((current.right, position * 2 + 1))
            result = max(result, max_index - min_index + 1)
        return result
