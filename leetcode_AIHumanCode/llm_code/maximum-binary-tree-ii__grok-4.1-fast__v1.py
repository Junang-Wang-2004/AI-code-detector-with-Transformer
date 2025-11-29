# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if root.val < val:
            temp = TreeNode(val)
            temp.left = root
            return temp
        if root.right is None or root.right.val <= val:
            temp = TreeNode(val)
            temp.left = root.right
            root.right = temp
            return root
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
