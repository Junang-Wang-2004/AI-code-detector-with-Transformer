class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            current, level = queue.popleft()
            if not current.left and not current.right:
                return level
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
