class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        def helper(lnode, rnode):
            if not lnode or not rnode:
                return lnode == rnode
            return (lnode.val == rnode.val and
                    helper(lnode.left, rnode.right) and
                    helper(lnode.right, rnode.left))
        return bool(root) == False or helper(root.left, root.right)
