class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        stk = [(root, root.val)]
        while stk:
            curr, total = stk.pop()
            if not curr.left and not curr.right:
                if total == target:
                    return True
            if curr.right:
                stk.append((curr.right, total + curr.right.val))
            if curr.left:
                stk.append((curr.left, total + curr.left.val))
        return False
