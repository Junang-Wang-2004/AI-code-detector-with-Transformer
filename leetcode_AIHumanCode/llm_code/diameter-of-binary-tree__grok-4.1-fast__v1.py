class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        max_path = 0
        def traverse(curr):
            nonlocal max_path
            if not curr:
                return 0
            l_depth = traverse(curr.left)
            r_depth = traverse(curr.right)
            max_path = max(max_path, l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        traverse(root)
        return max_path
