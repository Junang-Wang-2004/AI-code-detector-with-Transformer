class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        pos = root
        while True:
            if val <= pos.val:
                if pos.left is None:
                    pos.left = TreeNode(val)
                    return root
                pos = pos.left
            else:
                if pos.right is None:
                    pos.right = TreeNode(val)
                    return root
                pos = pos.right
