from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None
        queue = deque([root])
        while queue:
            level_length = len(queue)
            candidate = None
            for _ in range(level_length):
                current = queue.popleft()
                if candidate is None:
                    candidate = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return candidate
