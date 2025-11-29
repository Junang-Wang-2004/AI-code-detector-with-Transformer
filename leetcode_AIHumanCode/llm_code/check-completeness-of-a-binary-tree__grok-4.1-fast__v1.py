from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root):
        q = deque([root])
        missing = False
        while q:
            node = q.popleft()
            if missing and node:
                return False
            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                missing = True
        return True
