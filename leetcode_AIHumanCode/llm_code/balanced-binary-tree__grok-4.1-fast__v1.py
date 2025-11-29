class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        def validate(node):
            if not node:
                return True, 0
            left_ok, left_h = validate(node.left)
            right_ok, right_h = validate(node.right)
            if not left_ok or not right_ok:
                return False, 0
            diff = abs(left_h - right_h)
            current_ok = diff <= 1
            height = max(left_h, right_h) + 1
            return current_ok, height
        ok, _ = validate(root)
        return ok
