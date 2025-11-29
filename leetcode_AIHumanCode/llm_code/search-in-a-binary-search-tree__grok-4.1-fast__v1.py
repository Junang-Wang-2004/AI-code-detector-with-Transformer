class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, node, target):
        if node is None or node.val == target:
            return node
        if target < node.val:
            return self.searchBST(node.left, target)
        return self.searchBST(node.right, target)
