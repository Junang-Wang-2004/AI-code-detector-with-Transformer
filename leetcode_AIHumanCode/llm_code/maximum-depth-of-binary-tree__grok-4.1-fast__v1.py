class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        result = 0
        while stack:
            curr, dep = stack.pop()
            result = max(result, dep)
            if curr.right:
                stack.append((curr.right, dep + 1))
            if curr.left:
                stack.append((curr.left, dep + 1))
        return result
