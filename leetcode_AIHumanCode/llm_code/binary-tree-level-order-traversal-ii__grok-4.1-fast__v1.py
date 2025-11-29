class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        levels = []
        while queue:
            size = len(queue)
            current_level = []
            for _ in range(size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)
        levels.reverse()
        return levels
