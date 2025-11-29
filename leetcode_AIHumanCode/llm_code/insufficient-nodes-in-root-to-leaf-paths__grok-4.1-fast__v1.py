class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def sufficientSubset(self, root, limit):
        def has_path(node, req):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val >= req
            left_good = has_path(node.left, req - node.val)
            right_good = has_path(node.right, req - node.val)
            if not left_good:
                node.left = None
            if not right_good:
                node.right = None
            return left_good or right_good

        if has_path(root, limit):
            return root
        return None
