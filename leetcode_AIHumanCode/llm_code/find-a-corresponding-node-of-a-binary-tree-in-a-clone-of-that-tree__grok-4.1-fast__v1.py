class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, source, replica, objective):
        def traverse(a, b):
            if a is None:
                return None
            if a == objective:
                return b
            result = traverse(a.left, b.left)
            if result is not None:
                return result
            return traverse(a.right, b.right)
        return traverse(source, replica)
