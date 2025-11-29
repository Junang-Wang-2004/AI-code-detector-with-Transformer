class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        stk = [(root, root.val)]
        res = 0
        while stk:
            curr, prefix = stk.pop()
            if not curr.left and not curr.right:
                res += prefix
                continue
            if curr.right:
                stk.append((curr.right, prefix * 10 + curr.right.val))
            if curr.left:
                stk.append((curr.left, prefix * 10 + curr.left.val))
        return res
