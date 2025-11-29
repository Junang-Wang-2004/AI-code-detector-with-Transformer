class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        res = 0
        stk = [(root, root.val, root.val)] if root else []
        while stk:
            node, pmax, pmin = stk.pop()
            diff1 = pmax - node.val
            diff2 = node.val - pmin
            res = max(res, diff1, diff2)
            cmax = max(pmax, node.val)
            cmin = min(pmin, node.val)
            if node.left:
                stk.append((node.left, cmax, cmin))
            if node.right:
                stk.append((node.right, cmax, cmin))
        return res
